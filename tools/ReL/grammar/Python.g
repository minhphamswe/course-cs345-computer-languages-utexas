/* Student: Minh Pham
 * EID: mlp2279
 * CSID: minhpham
 * Section: TTh 5:00-6:30pm
 * TA: benself
 */

/*
 [The 'BSD licence']
 Copyright (c) 2004 Terence Parr and Loring Craymer
 All rights reserved.

 Redistribution and use in source and binary forms, with or without
 modification, are permitted provided that the following conditions
 are met:
 1. Redistributions of source code must retain the above copyright
    notice, this list of conditions and the following disclaimer.
 2. Redistributions in binary form must reproduce the above copyright
    notice, this list of conditions and the following disclaimer in the
    documentation and/or other materials provided with the distribution.
 3. The name of the author may not be used to endorse or promote products
    derived from this software without specific prior written permission.

 THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
 IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
 OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
 IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
 INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
 NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
 DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
 THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
 THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/

/** Python 2.3.3 Grammar
 *
 *  Terence Parr and Loring Craymer
 *  February 2004
 *
 *  Converted to ANTLR v3 November 2005 by Terence Parr.
 *
 *  This grammar was derived automatically from the Python 2.3.3
 *  parser grammar to get a syntactically correct ANTLR grammar
 *  for Python.  Then Terence hand tweaked it to be semantically
 *  correct; i.e., removed lookahead issues etc...  It is LL(1)
 *  except for the (sometimes optional) trailing commas and semi-colons.
 *  It needs two symbols of lookahead in this case.
 *
 *  Starting with Loring's preliminary lexer for Python, I modified it
 *  to do my version of the whole nasty INDENT/DEDENT issue just so I
 *  could understand the problem better.  This grammar requires
 *  PythonTokenStream.java to work.  Also I used some rules from the
 *  semi-formal grammar on the web for Python (automatically
 *  translated to ANTLR format by an ANTLR grammar, naturally <grin>).
 *  The lexical rules for python are particularly nasty and it took me
 *  a long time to get it 'right'; i.e., think about it in the proper
 *  way.  Resist changing the lexer unless you've used ANTLR a lot. ;)
 *
 *  I (Terence) tested this by running it on the jython-2.1/Lib
 *  directory of 40k lines of Python.
 *
 *  REQUIRES ANTLR v3
 *
 *
 *  Updated the original parser for Python 2.5 features. The parser has been
 *  altered to produce an AST - the AST work started from tne newcompiler
 *  grammar from Jim Baker.  The current parsing and compiling strategy looks
 *  like this:
 *
 *  Python source->Python.g->AST (org/python/parser/ast/*)->CodeCompiler(ASM)->.class
 */

grammar Python;
options {
    ASTLabelType=PythonTree;
    output=AST;
}

tokens {
    INDENT;
    DEDENT;
    TRAILBACKSLASH; //For dangling backslashes when partial parsing.
}
scope connection
{
	String url;
	String uname;
	String pword;
	String contype;
}
@header {
package org.python.antlr;

import org.antlr.runtime.CommonToken;

import org.python.antlr.ParseException;
import org.python.antlr.PythonTree;
import org.python.antlr.ast.alias;
import org.python.antlr.ast.arguments;
import org.python.antlr.ast.Assert;
import org.python.antlr.ast.Assign;
import org.python.antlr.ast.Attribute;
import org.python.antlr.ast.AugAssign;
import org.python.antlr.ast.BinOp;
import org.python.antlr.ast.BoolOp;
import org.python.antlr.ast.boolopType;
import org.python.antlr.ast.Break;
import org.python.antlr.ast.Call;
import org.python.antlr.ast.ClassDef;
import org.python.antlr.ast.cmpopType;
import org.python.antlr.ast.Compare;
import org.python.antlr.ast.comprehension;
import org.python.antlr.ast.Context;
import org.python.antlr.ast.Continue;
import org.python.antlr.ast.Delete;
import org.python.antlr.ast.Dict;
import org.python.antlr.ast.Ellipsis;
import org.python.antlr.ast.ErrorMod;
import org.python.antlr.ast.ExceptHandler;
import org.python.antlr.ast.Exec;
import org.python.antlr.ast.Expr;
import org.python.antlr.ast.Expression;
import org.python.antlr.ast.expr_contextType;
import org.python.antlr.ast.ExtSlice;
import org.python.antlr.ast.For;
import org.python.antlr.ast.GeneratorExp;
import org.python.antlr.ast.Global;
import org.python.antlr.ast.If;
import org.python.antlr.ast.IfExp;
import org.python.antlr.ast.Import;
import org.python.antlr.ast.ImportFrom;
import org.python.antlr.ast.Index;
import org.python.antlr.ast.Interactive;
import org.python.antlr.ast.keyword;
import org.python.antlr.ast.ListComp;
import org.python.antlr.ast.Lambda;
import org.python.antlr.ast.Module;
import org.python.antlr.ast.Name;
import org.python.antlr.ast.Num;
import org.python.antlr.ast.operatorType;
import org.python.antlr.ast.Pass;
import org.python.antlr.ast.Print;
import org.python.antlr.ast.Raise;
import org.python.antlr.ast.Repr;
import org.python.antlr.ast.Return;
import org.python.antlr.ast.Slice;
import org.python.antlr.ast.Str;
import org.python.antlr.ast.Subscript;
import org.python.antlr.ast.TryExcept;
import org.python.antlr.ast.TryFinally;
import org.python.antlr.ast.Tuple;
import org.python.antlr.ast.unaryopType;
import org.python.antlr.ast.UnaryOp;
import org.python.antlr.ast.While;
import org.python.antlr.ast.With;
import org.python.antlr.ast.Yield;
import org.python.antlr.base.excepthandler;
import org.python.antlr.base.expr;
import org.python.antlr.base.mod;
import org.python.antlr.base.slice;
import org.python.antlr.base.stmt;
import org.python.core.Py;
import org.python.core.PyObject;
import org.python.core.PyString;
import org.python.core.PyUnicode;

import java.math.BigInteger;
import java.util.Collections;
import java.util.Iterator;
import java.util.ListIterator;

import java.util.LinkedList;
import org.python.antlr.ast.Connection;
}

@members {
    private ErrorHandler errorHandler;

    private GrammarActions actions = new GrammarActions();

    private String encoding;

    public void setErrorHandler(ErrorHandler eh) {
        this.errorHandler = eh;
        actions.setErrorHandler(eh);
    }

    protected Object recoverFromMismatchedToken(IntStream input, int ttype, BitSet follow)
        throws RecognitionException {

        Object o = errorHandler.recoverFromMismatchedToken(this, input, ttype, follow);
        if (o != null) {
            return o;
        }
        return super.recoverFromMismatchedToken(input, ttype, follow);
    }

    public PythonParser(TokenStream input, String encoding) {
        this(input);
        this.encoding = encoding;
    }

}

@rulecatch {
catch (RecognitionException re) {
    errorHandler.reportError(this, re);
    errorHandler.recover(this, input,re);
    retval.tree = (PythonTree)adaptor.errorNode(input, retval.start, input.LT(-1), re);
}
}

@lexer::header {
package org.python.antlr;
}

@lexer::members {
/** Handles context-sensitive lexing of implicit line joining such as
 *  the case where newline is ignored in cases like this:
 *  a = [3,
 *       4]
 */
int implicitLineJoiningLevel = 0;
int startPos=-1;

//For use in partial parsing.
public boolean eofWhileNested = false;
public boolean partial = false;
public boolean single = false;

//If you want to use another error recovery mechanism change this
//and the same one in the parser.
private ErrorHandler errorHandler;

    public void setErrorHandler(ErrorHandler eh) {
        this.errorHandler = eh;
    }

    /**
     *  Taken directly from antlr's Lexer.java -- needs to be re-integrated every time
     *  we upgrade from Antlr (need to consider a Lexer subclass, though the issue would
     *  remain).
     */
    public Token nextToken() {
        startPos = getCharPositionInLine();
        while (true) {
            state.token = null;
            state.channel = Token.DEFAULT_CHANNEL;
            state.tokenStartCharIndex = input.index();
            state.tokenStartCharPositionInLine = input.getCharPositionInLine();
            state.tokenStartLine = input.getLine();
            state.text = null;
            if ( input.LA(1)==CharStream.EOF ) {
                if (implicitLineJoiningLevel > 0) {
                    eofWhileNested = true;
                }
                return Token.EOF_TOKEN;
            }
            try {
                mTokens();
                if ( state.token==null ) {
                    emit();
                }
                else if ( state.token==Token.SKIP_TOKEN ) {
                    continue;
                }
                return state.token;
            } catch (NoViableAltException nva) {
                errorHandler.reportError(this, nva);
                errorHandler.recover(this, nva); // throw out current char and try again
            } catch (FailedPredicateException fp) {
                //XXX: added this for failed STRINGPART -- the FailedPredicateException
                //     hides a NoViableAltException.  This should be the only
                //     FailedPredicateException that gets thrown by the lexer.
                errorHandler.reportError(this, fp);
                errorHandler.recover(this, fp); // throw out current char and try again
            } catch (RecognitionException re) {
                errorHandler.reportError(this, re);
                // match() routine has already called recover()
            }
        }
    }
}

//START OF PARSER RULES

//single_input: NEWLINE | simple_stmt | compound_stmt NEWLINE
single_input
@init {
    mod mtype = null;
}
@after {
    $single_input.tree = mtype;
}
    : NEWLINE* EOF
      {
        mtype = new Interactive($single_input.start, new ArrayList<stmt>());
      }
    | simple_stmt NEWLINE* EOF
      {
        mtype = new Interactive($single_input.start, actions.castStmts($simple_stmt.stypes));
      }
    | compound_stmt NEWLINE+ EOF
      {
        mtype = new Interactive($single_input.start, actions.castStmts($compound_stmt.tree));
      }
    ;
    //XXX: this block is duplicated in three places, how to extract?
    catch [RecognitionException re] {
        errorHandler.reportError(this, re);
        errorHandler.recover(this, input,re);
        PythonTree badNode = (PythonTree)adaptor.errorNode(input, retval.start, input.LT(-1), re);
        retval.tree = new ErrorMod(badNode);
    }

//file_input: (NEWLINE | stmt)* ENDMARKER
file_input
@init {
    mod mtype = null;
    List stypes = new ArrayList();
}
@after {
    if (!stypes.isEmpty()) {
        //The EOF token messes up the end offsets, so set them manually.
        //XXX: this may no longer be true now that PythonTokenSource is
        //     adjusting EOF offsets -- but needs testing before I remove
        //     this.
        PythonTree stop = (PythonTree)stypes.get(stypes.size() -1);
        mtype.setCharStopIndex(stop.getCharStopIndex());
        mtype.setTokenStopIndex(stop.getTokenStopIndex());
    }

    $file_input.tree = mtype;
}
    : (NEWLINE
      | stmt
      {
          if ($stmt.stypes != null) {
              stypes.addAll($stmt.stypes);
          }
      }
      )* EOF
         {
             mtype = new Module($file_input.start, actions.castStmts(stypes));
         }
    ;
    //XXX: this block is duplicated in three places, how to extract?
    catch [RecognitionException re] {
        errorHandler.reportError(this, re);
        errorHandler.recover(this, input,re);
        PythonTree badNode = (PythonTree)adaptor.errorNode(input, retval.start, input.LT(-1), re);
        retval.tree = new ErrorMod(badNode);
    }

//eval_input: testlist NEWLINE* ENDMARKER
eval_input
@init {
    mod mtype = null;
}
@after {
    $eval_input.tree = mtype;
}
    : LEADING_WS? (NEWLINE)* testlist[expr_contextType.Load] (NEWLINE)* EOF
      {
        mtype = new Expression($eval_input.start, actions.castExpr($testlist.tree));
      }
    ;
    //XXX: this block is duplicated in three places, how to extract?
    catch [RecognitionException re] {
        errorHandler.reportError(this, re);
        errorHandler.recover(this, input,re);
        PythonTree badNode = (PythonTree)adaptor.errorNode(input, retval.start, input.LT(-1), re);
        retval.tree = new ErrorMod(badNode);
    }


//not in CPython's Grammar file
dotted_attr
    returns [expr etype]
    : n1=NAME
      ( (DOT n2+=NAME)+
        {
            $etype = actions.makeDottedAttr($n1, $n2);
        }
      |
        {
            $etype = actions.makeNameNode($n1);
        }
      )
    ;

//attr is here for Java  compatibility.  A Java foo.getIf() can be called from Jython as foo.if
//     so we need to support any keyword as an attribute.

attr
    : NAME
    | AND
    | AS
    | ASSERT
    | BREAK
    | CLASS
    | CONTINUE
    | DEF
    | DELETE
    | ELIF
    | EXCEPT
    | EXEC
    | FINALLY
    | FROM
    | FOR
    | GLOBAL
    | IF
    | IMPORT
    | IN
    | IS
    | LAMBDA
    | NOT
    | OR
    | ORELSE
    | PASS
    | PRINT
    | RAISE
    | RETURN
    | TRY
    | WHILE
    | WITH
    | YIELD
    ;

//decorator: '@' dotted_name [ '(' [arglist] ')' ] NEWLINE
decorator
    returns [expr etype]
@after {
   $decorator.tree = $etype;
}
    : AT dotted_attr
    ( LPAREN
      ( arglist
        {
            $etype = actions.makeCall($LPAREN, $dotted_attr.etype, $arglist.args, $arglist.keywords,
                     $arglist.starargs, $arglist.kwargs);
        }
      |
        {
            $etype = actions.makeCall($LPAREN, $dotted_attr.etype);
        }
      )
      RPAREN
    |
      {
          $etype = $dotted_attr.etype;
      }
    ) NEWLINE
    ;

//decorators: decorator+
decorators
    returns [List etypes]
    : d+=decorator+
      {
          $etypes = $d;
      }
    ;

//funcdef: [decorators] 'def' NAME parameters ':' suite
funcdef
@init {
    stmt stype = null;
}

@after {
    $funcdef.tree = stype;
}
    : decorators? DEF NAME parameters COLON suite[false]
    {
        Token t = $DEF;
        if ($decorators.start != null) {
            t = $decorators.start;
        }
        stype = actions.makeFuncdef(t, $NAME, $parameters.args, $suite.stypes, $decorators.etypes);
    }
    ;

//parameters: '(' [varargslist] ')'
parameters
    returns [arguments args]
    : LPAREN
      (varargslist
        {
              $args = $varargslist.args;
        }
      |
        {
            $args = new arguments($parameters.start, new ArrayList<expr>(), null, null, new ArrayList<expr>());
        }
      )
      RPAREN
    ;

//not in CPython's Grammar file
defparameter
    [List defaults] returns [expr etype]
@after {
   $defparameter.tree = $etype;
}
    : fpdef[expr_contextType.Param] (ASSIGN test[expr_contextType.Load])?
      {
          $etype = actions.castExpr($fpdef.tree);
          if ($ASSIGN != null) {
              defaults.add($test.tree);
          } else if (!defaults.isEmpty()) {
              throw new ParseException("non-default argument follows default argument", $fpdef.tree);
          }
      }
    ;

//varargslist: ((fpdef ['=' test] ',')*
//              ('*' NAME [',' '**' NAME] | '**' NAME) |
//              fpdef ['=' test] (',' fpdef ['=' test])* [','])
varargslist
    returns [arguments args]
@init {
    List defaults = new ArrayList();
}
    : d+=defparameter[defaults] (options {greedy=true;}:COMMA d+=defparameter[defaults])*
      (COMMA
          (STAR starargs=NAME (COMMA DOUBLESTAR kwargs=NAME)?
          | DOUBLESTAR kwargs=NAME
          )?
      )?
      {
          $args = actions.makeArgumentsType($varargslist.start, $d, $starargs, $kwargs, defaults);
      }
    | STAR starargs=NAME (COMMA DOUBLESTAR kwargs=NAME)?
      {
          $args = actions.makeArgumentsType($varargslist.start, $d, $starargs, $kwargs, defaults);
      }
    | DOUBLESTAR kwargs=NAME
      {
          $args = actions.makeArgumentsType($varargslist.start, $d, null, $kwargs, defaults);
      }
    ;

//fpdef: NAME | '(' fplist ')'
fpdef[expr_contextType ctype]
@init {
    expr etype = null;
}
@after {
    if (etype != null) {
        $fpdef.tree = etype;
    }
    actions.checkAssign(actions.castExpr($fpdef.tree));
}
    : NAME
      {
          etype = new Name($NAME, $NAME.text, ctype);
      }
    | (LPAREN fpdef[null] COMMA) => LPAREN fplist RPAREN
      {
          etype = new Tuple($fplist.start, actions.castExprs($fplist.etypes), expr_contextType.Store);
      }
    | LPAREN! fplist RPAREN!
    ;

//fplist: fpdef (',' fpdef)* [',']
fplist
    returns [List etypes]
    : f+=fpdef[expr_contextType.Store]
      (options {greedy=true;}:COMMA f+=fpdef[expr_contextType.Store])* (COMMA)?
      {
          $etypes = $f;
      }
    ;

//stmt: simple_stmt | compound_stmt
stmt
    returns [List stypes]
    : simple_stmt
      {
          $stypes = $simple_stmt.stypes;
      }
    | compound_stmt
      {
          $stypes = new ArrayList();
          $stypes.add($compound_stmt.tree);
      }
    ;

//simple_stmt: small_stmt (';' small_stmt)* [';'] NEWLINE
simple_stmt
    returns [List stypes]
    : s+=small_stmt (options {greedy=true;}:SEMI s+=small_stmt)* (SEMI)? NEWLINE
      {
          $stypes = $s;
      }
    ;

//small_stmt: (expr_stmt | print_stmt  | del_stmt | pass_stmt | flow_stmt |
//             import_stmt | global_stmt | exec_stmt | assert_stmt)
small_stmt : expr_stmt
           | print_stmt
           | del_stmt
           | pass_stmt
           | flow_stmt
           | import_stmt
           | global_stmt
           | exec_stmt
           | assert_stmt
           ;

//expr_stmt: testlist (augassign (yield_expr|testlist) |
//                     ('=' (yield_expr|testlist))*)
expr_stmt
@init {
    stmt stype = null;
}
@after {
    if (stype != null) {
        $expr_stmt.tree = stype;
    }
}
    : ((testlist[null] augassign) => lhs=testlist[expr_contextType.AugStore]
        ( (aay=augassign y1=yield_expr
           {
               actions.checkAssign(actions.castExpr($lhs.tree));
               stype = new AugAssign($lhs.tree, actions.castExpr($lhs.tree), $aay.op, actions.castExpr($y1.etype));
           }
          )
        | (aat=augassign rhs=testlist[expr_contextType.Load]
           {
               actions.checkAssign(actions.castExpr($lhs.tree));
               stype = new AugAssign($lhs.tree, actions.castExpr($lhs.tree), $aat.op, actions.castExpr($rhs.tree));
           }
          )
        )
    | (testlist[null] ASSIGN) => lhs=testlist[expr_contextType.Store]
        (
        | ((at=ASSIGN t+=testlist[expr_contextType.Store])+
            {
                stype = new Assign($lhs.tree, actions.makeAssignTargets(
                    actions.castExpr($lhs.tree), $t), actions.makeAssignValue($t));
            }
          )
        | ((ay=ASSIGN y2+=yield_expr)+
            {
                stype = new Assign($lhs.start, actions.makeAssignTargets(
                    actions.castExpr($lhs.tree), $y2), actions.makeAssignValue($y2));
            }
          )
        )
    | lhs=testlist[expr_contextType.Load]
      {
          stype = new Expr($lhs.start, actions.castExpr($lhs.tree));
      }
    )
    ;

//augassign: ('+=' | '-=' | '*=' | '/=' | '%=' | '&=' | '|=' | '^=' |
//            '<<=' | '>>=' | '**=' | '//=')
augassign
    returns [operatorType op]
    : PLUSEQUAL
        {
            $op = operatorType.Add;
        }
    | MINUSEQUAL
        {
            $op = operatorType.Sub;
        }
    | STAREQUAL
        {
            $op = operatorType.Mult;
        }
    | SLASHEQUAL
        {
            $op = operatorType.Div;
        }
    | PERCENTEQUAL
        {
            $op = operatorType.Mod;
        }
    | AMPEREQUAL
        {
            $op = operatorType.BitAnd;
        }
    | VBAREQUAL
        {
            $op = operatorType.BitOr;
        }
    | CIRCUMFLEXEQUAL
        {
            $op = operatorType.BitXor;
        }
    | LEFTSHIFTEQUAL
        {
            $op = operatorType.LShift;
        }
    | RIGHTSHIFTEQUAL
        {
            $op = operatorType.RShift;
        }
    | DOUBLESTAREQUAL
        {
            $op = operatorType.Pow;
        }
    | DOUBLESLASHEQUAL
        {
            $op = operatorType.FloorDiv;
        }
    ;

//print_stmt: 'print' ( [ test (',' test)* [','] ] |
//                      '>>' test [ (',' test)+ [','] ] )
print_stmt
@init {
    stmt stype = null;
}

@after {
    $print_stmt.tree = stype;
}
    : PRINT
      (t1=printlist
       {
           stype = new Print($PRINT, null, actions.castExprs($t1.elts), $t1.newline);
       }
      | RIGHTSHIFT t2=printlist2
       {
           stype = new Print($PRINT, actions.castExpr($t2.elts.get(0)), actions.castExprs($t2.elts, 1), $t2.newline);
       }
      |
       {
           stype = new Print($PRINT, null, new ArrayList<expr>(), true);
       }
      )
      ;

//not in CPython's Grammar file
printlist
    returns [boolean newline, List elts]
    : (test[null] COMMA) =>
       t+=test[expr_contextType.Load] (options {k=2;}: COMMA t+=test[expr_contextType.Load])* (trailcomma=COMMA)?
       {
           $elts=$t;
           if ($trailcomma == null) {
               $newline = true;
           } else {
               $newline = false;
           }
       }
    | t+=test[expr_contextType.Load]
      {
          $elts=$t;
          $newline = true;
      }
    ;

//XXX: would be nice if printlist and printlist2 could be merged.
//not in CPython's Grammar file
printlist2
    returns [boolean newline, List elts]
    : (test[null] COMMA test[null]) =>
       t+=test[expr_contextType.Load] (options {k=2;}: COMMA t+=test[expr_contextType.Load])* (trailcomma=COMMA)?
       { $elts=$t;
           if ($trailcomma == null) {
               $newline = true;
           } else {
               $newline = false;
           }
       }
    | t+=test[expr_contextType.Load]
      {
          $elts=$t;
          $newline = true;
      }
    ;

//del_stmt: 'del' exprlist
del_stmt
@init {
    stmt stype = null;
}
@after {
   $del_stmt.tree = stype;
}
    : DELETE del_list
      {
          stype = new Delete($DELETE, $del_list.etypes);
      }
    ;

//pass_stmt: 'pass'
pass_stmt
@init {
    stmt stype = null;
}
@after {
   $pass_stmt.tree = stype;
}
    : PASS
      {
          stype = new Pass($PASS);
      }
    ;

//flow_stmt: break_stmt | continue_stmt | return_stmt | raise_stmt | yield_stmt
flow_stmt
    : break_stmt
    | continue_stmt
    | return_stmt
    | raise_stmt
    | yield_stmt
    ;

//break_stmt: 'break'
break_stmt
@init {
    stmt stype = null;
}
@after {
   $break_stmt.tree = stype;
}
    : BREAK
      {
          stype = new Break($BREAK);
      }
    ;

//continue_stmt: 'continue'
continue_stmt
@init {
    stmt stype = null;
}
@after {
   $continue_stmt.tree = stype;
}
    : CONTINUE
      {
          if (!$suite.isEmpty() && $suite::continueIllegal) {
              errorHandler.error("'continue' not supported inside 'finally' clause", new PythonTree($continue_stmt.start));
          }
          stype = new Continue($CONTINUE);
      }
    ;

//return_stmt: 'return' [testlist]
return_stmt
@init {
    stmt stype = null;
}
@after {
   $return_stmt.tree = stype;
}
    : RETURN
      (testlist[expr_contextType.Load]
       {
           stype = new Return($RETURN, actions.castExpr($testlist.tree));
       }
      |
       {
           stype = new Return($RETURN, null);
       }
      )
      ;

//yield_stmt: yield_expr
yield_stmt
@init {
    stmt stype = null;
}
@after {
   $yield_stmt.tree = stype;
}
    : yield_expr
      {
        stype = new Expr($yield_expr.start, actions.castExpr($yield_expr.etype));
      }
    ;

//raise_stmt: 'raise' [test [',' test [',' test]]]
raise_stmt
@init {
    stmt stype = null;
}
@after {
   $raise_stmt.tree = stype;
}
    : RAISE (t1=test[expr_contextType.Load] (COMMA t2=test[expr_contextType.Load]
        (COMMA t3=test[expr_contextType.Load])?)?)?
      {
          stype = new Raise($RAISE, actions.castExpr($t1.tree), actions.castExpr($t2.tree), actions.castExpr($t3.tree));
      }
    ;

//import_stmt: import_name | import_from
import_stmt
    : import_name
    | import_from
    ;

//import_name: 'import' dotted_as_names
import_name
@init {
    stmt stype = null;
}
@after {
   $import_name.tree = stype;
}
    : IMPORT dotted_as_names
      {
          stype = new Import($IMPORT, $dotted_as_names.atypes);
      }
    ;

//import_from: ('from' ('.'* dotted_name | '.'+)
//              'import' ('*' | '(' import_as_names ')' | import_as_names))
import_from
@init {
    stmt stype = null;
}
@after {
   $import_from.tree = stype;
}
    : FROM (d+=DOT* dotted_name | d+=DOT+) IMPORT
        (STAR
         {
             stype = new ImportFrom($FROM, actions.makeFromText($d, $dotted_name.names),
                 actions.makeModuleNameNode($d, $dotted_name.names),
                 actions.makeStarAlias($STAR), actions.makeLevel($d));
         }
        | i1=import_as_names
         {
             stype = new ImportFrom($FROM, actions.makeFromText($d, $dotted_name.names),
                 actions.makeModuleNameNode($d, $dotted_name.names),
                 actions.makeAliases($i1.atypes), actions.makeLevel($d));
         }
        | LPAREN i2=import_as_names COMMA? RPAREN
         {
             stype = new ImportFrom($FROM, actions.makeFromText($d, $dotted_name.names),
                 actions.makeModuleNameNode($d, $dotted_name.names),
                 actions.makeAliases($i2.atypes), actions.makeLevel($d));
         }
        )
    ;

//import_as_names: import_as_name (',' import_as_name)* [',']
import_as_names
    returns [List<alias> atypes]
    : n+=import_as_name (COMMA! n+=import_as_name)*
    {
        $atypes = $n;
    }
    ;

//import_as_name: NAME [('as' | NAME) NAME]
import_as_name
    returns [alias atype]
@after {
    $import_as_name.tree = $atype;
}
    : name=NAME (AS asname=NAME)?
    {
        $atype = new alias(actions.makeNameNode($name), actions.makeNameNode($asname));
    }
    ;

//XXX: when does CPython Grammar match "dotted_name NAME NAME"?
//dotted_as_name: dotted_name [('as' | NAME) NAME]
dotted_as_name
    returns [alias atype]
@after {
    $dotted_as_name.tree = $atype;
}
    : dotted_name (AS asname=NAME)?
    {
        $atype = new alias($dotted_name.names, actions.makeNameNode($asname));
    }
    ;

//dotted_as_names: dotted_as_name (',' dotted_as_name)*
dotted_as_names
    returns [List<alias> atypes]
    : d+=dotted_as_name (COMMA! d+=dotted_as_name)*
    {
        $atypes = $d;
    }
    ;

//dotted_name: NAME ('.' NAME)*
dotted_name
    returns [List<Name> names]
    : NAME (DOT dn+=attr)*
    {
        $names = actions.makeDottedName($NAME, $dn);
    }
    ;

//global_stmt: 'global' NAME (',' NAME)*
global_stmt
@init {
    stmt stype = null;
}
@after {
   $global_stmt.tree = stype;
}
    : GLOBAL n+=NAME (COMMA n+=NAME)*
      {
          stype = new Global($GLOBAL, actions.makeNames($n), actions.makeNameNodes($n));
      }
    ;

//exec_stmt: 'exec' expr ['in' test [',' test]]
exec_stmt
@init {
    stmt stype = null;
}
@after {
   $exec_stmt.tree = stype;
}
    : EXEC expr[expr_contextType.Load] (IN t1=test[expr_contextType.Load] (COMMA t2=test[expr_contextType.Load])?)?
      {
         stype = new Exec($EXEC, actions.castExpr($expr.tree), actions.castExpr($t1.tree), actions.castExpr($t2.tree));
      }
    ;

//assert_stmt: 'assert' test [',' test]
assert_stmt
@init {
    stmt stype = null;
}
@after {
   $assert_stmt.tree = stype;
}
    : ASSERT t1=test[expr_contextType.Load] (COMMA t2=test[expr_contextType.Load])?
      {
          stype = new Assert($ASSERT, actions.castExpr($t1.tree), actions.castExpr($t2.tree));
      }
    ;

//compound_stmt: if_stmt | while_stmt | for_stmt | try_stmt | funcdef | classdef
compound_stmt
    : if_stmt
    | while_stmt
    | for_stmt
    | try_stmt
    | with_stmt
    | (decorators? DEF) => funcdef
    | classdef
    ;

//if_stmt: 'if' test ':' suite ('elif' test ':' suite)* ['else' ':' suite]
if_stmt
@init {
    stmt stype = null;
}
@after {
   $if_stmt.tree = stype;
}
    : IF test[expr_contextType.Load] COLON ifsuite=suite[false] elif_clause?
      {
          stype = new If($IF, actions.castExpr($test.tree), actions.castStmts($ifsuite.stypes),
              actions.makeElse($elif_clause.stypes, $elif_clause.tree));
      }
    ;

//not in CPython's Grammar file
elif_clause
    returns [List stypes]
@init {
    stmt stype = null;
}
@after {
   if (stype != null) {
       $elif_clause.tree = stype;
   }
}
    : else_clause
      {
          $stypes = $else_clause.stypes;
      }
    | ELIF test[expr_contextType.Load] COLON suite[false]
      (e2=elif_clause
       {
           stype = new If($test.start, actions.castExpr($test.tree), actions.castStmts($suite.stypes), actions.makeElse($e2.stypes, $e2.tree));
       }
      |
       {
           stype = new If($test.start, actions.castExpr($test.tree), actions.castStmts($suite.stypes), new ArrayList<stmt>());
       }
      )
    ;

//not in CPython's Grammar file
else_clause
    returns [List stypes]
    : ORELSE COLON elsesuite=suite[false]
      {
          $stypes = $suite.stypes;
      }
    ;

//while_stmt: 'while' test ':' suite ['else' ':' suite]
while_stmt
@init {
    stmt stype = null;
}
@after {
   $while_stmt.tree = stype;
}
    : WHILE test[expr_contextType.Load] COLON s1=suite[false] (ORELSE COLON s2=suite[false])?
      {
          stype = actions.makeWhile($WHILE, actions.castExpr($test.tree), $s1.stypes, $s2.stypes);
      }
    ;

//for_stmt: 'for' exprlist 'in' testlist ':' suite ['else' ':' suite]
for_stmt
@init {
    stmt stype = null;
}
@after {
   $for_stmt.tree = stype;
}
    : FOR exprlist[expr_contextType.Store] IN testlist[expr_contextType.Load] COLON s1=suite[false]
        (ORELSE COLON s2=suite[false])?
      {
          stype = actions.makeFor($FOR, $exprlist.etype, actions.castExpr($testlist.tree), $s1.stypes, $s2.stypes);
      }
    ;

//try_stmt: ('try' ':' suite
//           ((except_clause ':' suite)+
//           ['else' ':' suite]
//           ['finally' ':' suite] |
//           'finally' ':' suite))
try_stmt
@init {
    stmt stype = null;
}
@after {
   $try_stmt.tree = stype;
}
    : TRY COLON trysuite=suite[!$suite.isEmpty() && $suite::continueIllegal]
      ( e+=except_clause+ (ORELSE COLON elsesuite=suite[!$suite.isEmpty() && $suite::continueIllegal])? (FINALLY COLON finalsuite=suite[true])?
        {
            stype = actions.makeTryExcept($TRY, $trysuite.stypes, $e, $elsesuite.stypes, $finalsuite.stypes);
        }
      | FINALLY COLON finalsuite=suite[true]
        {
            stype = actions.makeTryFinally($TRY, $trysuite.stypes, $finalsuite.stypes);
        }
      )
      ;

//with_stmt: 'with' test [ with_var ] ':' suite
with_stmt
@init {
    stmt stype = null;
}
@after {
   $with_stmt.tree = stype;
}
    : WITH test[expr_contextType.Load] (with_var)? COLON suite[false]
      {
          stype = new With($WITH, actions.castExpr($test.tree), $with_var.etype,
              actions.castStmts($suite.stypes));
      }
    ;

//with_var: ('as' | NAME) expr
with_var
    returns [expr etype]
    : (AS | NAME) expr[expr_contextType.Store]
      {
          $etype = actions.castExpr($expr.tree);
          actions.checkAssign($etype);
      }
    ;

//except_clause: 'except' [test [('as' | ',') test]]
except_clause
@init {
    excepthandler extype = null;
}
@after {
   $except_clause.tree = extype;
}
    : EXCEPT (t1=test[expr_contextType.Load] ((COMMA | AS) t2=test[expr_contextType.Store])?)? COLON suite[!$suite.isEmpty() && $suite::continueIllegal]
      {
          extype = new ExceptHandler($EXCEPT, actions.castExpr($t1.tree), actions.castExpr($t2.tree),
              actions.castStmts($suite.stypes));
      }
    ;

//suite: simple_stmt | NEWLINE INDENT stmt+ DEDENT
suite
    [boolean fromFinally] returns [List stypes]
scope {
    boolean continueIllegal;
}
@init {
    if ($suite::continueIllegal || fromFinally) {
        $suite::continueIllegal = true;
    } else {
        $suite::continueIllegal = false;
    }
    $stypes = new ArrayList();
}
    : simple_stmt
      {
          $stypes = $simple_stmt.stypes;
      }
    | NEWLINE INDENT
      (stmt
       {
           if ($stmt.stypes != null) {
               $stypes.addAll($stmt.stypes);
           }
       }
      )+ DEDENT
    ;

//test: or_test ['if' or_test 'else' test] | lambdef
test[expr_contextType ctype]
@init {
    expr etype = null;
}
@after {
   if (etype != null) {
       $test.tree = etype;
   }
}
    :o1=or_test[ctype]
      ( (IF or_test[null] ORELSE) => IF o2=or_test[ctype] ORELSE e=test[expr_contextType.Load]
         {
             etype = new IfExp($o1.start, actions.castExpr($o2.tree), actions.castExpr($o1.tree), actions.castExpr($e.tree));
         }
      |
     -> or_test
      )
    | lambdef
    ;

//or_test: and_test ('or' and_test)*
or_test
    [expr_contextType ctype] returns [Token leftTok]
@after {
    if ($or != null) {
        Token tok = $left.start;
        if ($left.leftTok != null) {
            tok = $left.leftTok;
        }
        $or_test.tree = actions.makeBoolOp(tok, $left.tree, boolopType.Or, $right);
    }
}
    : left=and_test[ctype]
        ( (or=OR right+=and_test[ctype]
          )+
        |
       -> $left
        )
    ;

//and_test: not_test ('and' not_test)*
and_test
    [expr_contextType ctype] returns [Token leftTok]
@after {
    if ($and != null) {
        Token tok = $left.start;
        if ($left.leftTok != null) {
            tok = $left.leftTok;
        }
        $and_test.tree = actions.makeBoolOp(tok, $left.tree, boolopType.And, $right);
    }
}
    : left=not_test[ctype]
        ( (and=AND right+=not_test[ctype]
          )+
        |
       -> $left
        )
    ;

//not_test: 'not' not_test | comparison
not_test
    [expr_contextType ctype] returns [Token leftTok]
@init {
    expr etype = null;
}
@after {
   if (etype != null) {
       $not_test.tree = etype;
   }
}
    : NOT nt=not_test[ctype]
      {
          etype = new UnaryOp($NOT, unaryopType.Not, actions.castExpr($nt.tree));
      }
    | comparison[ctype]
      {
          $leftTok = $comparison.leftTok;
      }
    ;

//comparison: expr (comp_op expr)*
comparison
    [expr_contextType ctype] returns [Token leftTok]
@init {
    List cmps = new ArrayList();
}
@after {
    $leftTok = $left.leftTok;
    if (!cmps.isEmpty()) {
        $comparison.tree = new Compare($left.start, actions.castExpr($left.tree), actions.makeCmpOps(cmps),
            actions.castExprs($right));
    }
}
    : left=expr[ctype]
       ( ( comp_op right+=expr[ctype]
           {
               cmps.add($comp_op.op);
           }
         )+
       |
      -> $left
       )
    ;

//comp_op: '<'|'>'|'=='|'>='|'<='|'<>'|'!='|'in'|'not' 'in'|'is'|'is' 'not'
comp_op
    returns [cmpopType op]
    : LESS
      {
          $op = cmpopType.Lt;
      }
    | GREATER
      {
          $op = cmpopType.Gt;
      }
    | EQUAL
      {
          $op = cmpopType.Eq;
      }
    | GREATEREQUAL
      {
          $op = cmpopType.GtE;
      }
    | LESSEQUAL
      {
          $op = cmpopType.LtE;
      }
    | ALT_NOTEQUAL
      {
          $op = cmpopType.NotEq;
      }
    | NOTEQUAL
      {
          $op = cmpopType.NotEq;
      }
    | IN
      {
          $op = cmpopType.In;
      }
    | NOT IN
      {
          $op = cmpopType.NotIn;
      }
    | IS
      {
          $op = cmpopType.Is;
      }
    | IS NOT
      {
          $op = cmpopType.IsNot;
      }
    ;

//expr: xor_expr ('|' xor_expr)*
expr
    [expr_contextType ect] returns [Token leftTok]
scope {
    expr_contextType ctype;
}
@init {
    $expr::ctype = ect;
}
@after {
    $leftTok = $left.lparen;
    if ($op != null) {
        Token tok = $left.start;
        if ($left.lparen != null) {
            tok = $left.lparen;
        }
        $expr.tree = actions.makeBinOp(tok, $left.tree, operatorType.BitOr, $right);
    }
}
    : left=xor_expr
        ( (op=VBAR right+=xor_expr
          )+
        |
       -> $left
        )
    ;


//xor_expr: and_expr ('^' and_expr)*
xor_expr
    returns [Token lparen = null]
@after {
    if ($op != null) {
        Token tok = $left.start;
        if ($left.lparen != null) {
            tok = $left.lparen;
        }
        $xor_expr.tree = actions.makeBinOp(tok, $left.tree, operatorType.BitXor, $right);
    }
    $lparen = $left.lparen;
}
    : left=and_expr
        ( (op=CIRCUMFLEX right+=and_expr
          )+
        |
       -> $left
        )
    ;

//and_expr: shift_expr ('&' shift_expr)*
and_expr
    returns [Token lparen = null]
@after {
    if ($op != null) {
        Token tok = $left.start;
        if ($left.lparen != null) {
            tok = $left.lparen;
        }
        $and_expr.tree = actions.makeBinOp(tok, $left.tree, operatorType.BitAnd, $right);
    }
    $lparen = $left.lparen;
}
    : left=shift_expr
        ( (op=AMPER right+=shift_expr
          )+
        |
       -> $left
        )
    ;

//shift_expr: arith_expr (('<<'|'>>') arith_expr)*
shift_expr
    returns [Token lparen = null]
@init {
    List ops = new ArrayList();
    List toks = new ArrayList();
}
@after {
    if (!ops.isEmpty()) {
        Token tok = $left.start;
        if ($left.lparen != null) {
            tok = $left.lparen;
        }
        $shift_expr.tree = actions.makeBinOp(tok, $left.tree, ops, $right, toks);
    }
    $lparen = $left.lparen;
}
    : left=arith_expr
        ( ( shift_op right+=arith_expr
            {
                ops.add($shift_op.op);
                toks.add($shift_op.start);
            }
          )+
        |
       -> $left
        )
    ;

shift_op
    returns [operatorType op]
    : LEFTSHIFT
      {
          $op = operatorType.LShift;
      }
    | RIGHTSHIFT
      {
          $op = operatorType.RShift;
      }
    ;

//arith_expr: term (('+'|'-') term)*
arith_expr
    returns [Token lparen = null]
@init {
    List ops = new ArrayList();
    List toks = new ArrayList();
}
@after {
    if (!ops.isEmpty()) {
        Token tok = $left.start;
        if ($left.lparen != null) {
            tok = $left.lparen;
        }
        $arith_expr.tree = actions.makeBinOp(tok, $left.tree, ops, $right, toks);
    }
    $lparen = $left.lparen;
}
    : left=term
        ( (arith_op right+=term
           {
               ops.add($arith_op.op);
               toks.add($arith_op.start);
           }
          )+
        |
       -> $left
        )
    ;
    // This only happens when Antlr is allowed to do error recovery (for example if ListErrorHandler
    // is used.  It is at least possible that this is a bug in Antlr itself, so this needs further
    // investigation.  To reproduce, set errorHandler to ListErrorHandler and try to parse "[".
    catch [RewriteCardinalityException rce] {
        PythonTree badNode = (PythonTree)adaptor.errorNode(input, retval.start, input.LT(-1), null);
        retval.tree = badNode;
        errorHandler.error("Internal Parser Error", badNode);
    }

arith_op
    returns [operatorType op]
    : PLUS
      {
          $op = operatorType.Add;
      }
    | MINUS
      {
          $op = operatorType.Sub;
      }
    ;

//term: factor (('*'|'/'|'%'|'//') factor)*
term
    returns [Token lparen = null]
@init {
    List ops = new ArrayList();
    List toks = new ArrayList();
}
@after {
    $lparen = $left.lparen;
    if (!ops.isEmpty()) {
        Token tok = $left.start;
        if ($left.lparen != null) {
            tok = $left.lparen;
        }
        $term.tree = actions.makeBinOp(tok, $left.tree, ops, $right, toks);
    }
}
    : left=factor
        ( (term_op right+=factor
          {
              ops.add($term_op.op);
              toks.add($term_op.start);
          }
          )+
        |
       -> $left
        )
    ;

term_op
    returns [operatorType op]
    : STAR
      {
          $op = operatorType.Mult;
      }
    | SLASH
      {
          $op = operatorType.Div;
      }
    | PERCENT
      {
          $op = operatorType.Mod;
      }
    | DOUBLESLASH
      {
          $op = operatorType.FloorDiv;
      }
    ;

//factor: ('+'|'-'|'~') factor | power
factor
    returns [expr etype, Token lparen = null]
@after {
    $factor.tree = $etype;
}
    : PLUS p=factor
      {
          $etype = new UnaryOp($PLUS, unaryopType.UAdd, $p.etype);
      }
    | MINUS m=factor
      {
          $etype = actions.negate($MINUS, $m.etype);
      }
    | TILDE t=factor
      {
          $etype = new UnaryOp($TILDE, unaryopType.Invert, $t.etype);
      }
    | power
      {
          $etype = actions.castExpr($power.tree);
          $lparen = $power.lparen;
      }
    ;

//power: atom trailer* ['**' factor]
power
    returns [expr etype, Token lparen = null]
@after {
    $power.tree = $etype;
}
    : atom (t+=trailer[$atom.start, $atom.tree])* (options {greedy=true;}:d=DOUBLESTAR factor)?
      {
          $lparen = $atom.lparen;
          //XXX: This could be better.
          $etype = actions.castExpr($atom.tree);
          if ($t != null) {
              for(Object o : $t) {
                  if ($etype instanceof Context) {
                      ((Context)$etype).setContext(expr_contextType.Load);
                  }
                  if (o instanceof Call) {
                      Call c = (Call)o;
                      c.setFunc((PyObject)$etype);
                      $etype = c;
                  } else if (o instanceof Subscript) {
                      Subscript c = (Subscript)o;
                      c.setValue((PyObject)$etype);
                      $etype = c;
                  } else if (o instanceof Attribute) {
                      Attribute c = (Attribute)o;
                      c.setCharStartIndex($etype.getCharStartIndex());
                      c.setValue((PyObject)$etype);
                      $etype = c;
                  }
              }
          }
          if ($d != null) {
              List right = new ArrayList();
              right.add($factor.tree);
              $etype = actions.makeBinOp($atom.start, $etype, operatorType.Pow, right);
          }
      }
    ;

//atom: ('(' [yield_expr|testlist_gexp] ')' |
//       '[' [listmaker] ']' |
//       '{' [dictmaker] '}' |
//       '`' testlist1 '`' |
//       NAME | NUMBER | STRING+)
atom
    returns [Token lparen = null]
@init {
    expr etype = null;
}
@after {
   if (etype != null) {
       $atom.tree = etype;
   }
}
    : LPAREN
      {
          $lparen = $LPAREN;
      }
      ( yield_expr
        {
            etype = $yield_expr.etype;
        }
      | testlist_gexp
     -> testlist_gexp
      |
        {
            etype = new Tuple($LPAREN, new ArrayList<expr>(), $expr::ctype);
        }
      )
      RPAREN
    | LBRACK
      (listmaker[$LBRACK]
     -> listmaker
      |
       {
           etype = new org.python.antlr.ast.List($LBRACK, new ArrayList<expr>(), $expr::ctype);
       }
      )
      RBRACK
    | LCURLY
       (dictmaker
        {
            etype = new Dict($LCURLY, actions.castExprs($dictmaker.keys),
              actions.castExprs($dictmaker.values));
        }
       |
        {
            etype = new Dict($LCURLY, new ArrayList<expr>(), new ArrayList<expr>());
        }
       )
       RCURLY
     | lb=BACKQUOTE testlist[expr_contextType.Load] rb=BACKQUOTE
       {
           etype = new Repr($lb, actions.castExpr($testlist.tree));
       }
     | NAME
       {
           etype = new Name($NAME, $NAME.text, $expr::ctype);
       }
     | INT
       {
           etype = new Num($INT, actions.makeInt($INT));
       }
     | LONGINT
       {
           etype = new Num($LONGINT, actions.makeInt($LONGINT));
       }
     | FLOAT
       {
           etype = new Num($FLOAT, actions.makeFloat($FLOAT));
       }
     | COMPLEX
       {
           etype = new Num($COMPLEX, actions.makeComplex($COMPLEX));
       }
     | (S+=STRING)+
       {
           etype = new Str(actions.extractStringToken($S), actions.extractStrings($S, encoding));
       }
     //make sqlstmt here, use tuple from testlist_gexp as example
    //might need to watch out for last test, not sure if that is requires at end bc of start state. 
    //maybe make dummy end expr somehow and put on tree?
    | sql_stmt
    ->sql_stmt
	//their prolog statements
	| prolog_stmt
	->prolog_stmt
	//checking for asp grammar
	| asp_stmt
	->asp_stmt
    | sim_stmt
    -> sim_stmt
    | sparql_stmt
    -> sparql_stmt
	;

/** Our prolog additions: prolog_load:  	PRO ?[expr].
											PRO ?[expr]+.
						  prolog_query: 	PRO ?-expr(expr*).
						  prolog_insert:	PRO ?->expr(expr*).
						  					PRO ?->expr(expr*):= expr(expr*)*.
						  prolog_save:		PRO ?>>[expr | CLEAR].
						  					PRO ?>>[expr | CLEAR]+.
						  */
prolog_stmt
scope{
	Boolean append;
	List exprs;
	List strings;
	String temp;
}
@init{
	expr etype = null;
}
@after {
	if (etype != null) {
		$prolog_stmt.tree = etype;
	}
}
	:
	{
		$prolog_stmt::append = false;
		$prolog_stmt::exprs = new ArrayList<expr>();
		$prolog_stmt::strings = new ArrayList<String>();
		$prolog_stmt::temp = "";
	}
    	(
    	(PRO PRLO{$prolog_stmt::strings.add($PRLO.text);} prologload RBRACK (PLUS {$prolog_stmt::append=true;})? DOT
    	{$prolog_stmt::strings.add($prolog_stmt::temp);}
	-> ^(PRLO<Tuple>[$prolog_stmt.start,actions.castExprs($prolog_stmt::exprs), $expr::ctype, $prolog_stmt::strings, $prolog_stmt::append, false,""]))
	|	(PRO ASPPRINTDB{$prolog_stmt::strings.add($ASPPRINTDB.text);}
	-> ^(ASPPRINTDB<Tuple>[$prolog_stmt.start,actions.castExprs($prolog_stmt::exprs), $expr::ctype, $prolog_stmt::strings, $prolog_stmt::append, false,""]))
	|	(PRO PRQO{$prolog_stmt::strings.add($PRQO.text);} prologquery DOT
		{$prolog_stmt::strings.add($prolog_stmt::temp+".");}
	-> ^(PRQO<Tuple>[$prolog_stmt.start, actions.castExprs($prolog_stmt::exprs), $expr::ctype, $prolog_stmt::strings, $prolog_stmt::append, false,""]))
	|	(PRO PRIO{$prolog_stmt::strings.add($PRIO.text);} prologinsert s2=DOT
		{$prolog_stmt::strings.add($prolog_stmt::temp+$s2.text);}
	-> ^(PRIO<Tuple>[$prolog_stmt.start, actions.castExprs($prolog_stmt::exprs), $expr::ctype, $prolog_stmt::strings, $prolog_stmt::append, false,""]))
	|	(PRO PRSO{$prolog_stmt::strings.add($PRSO.text);} prologsave RBRACK (PLUS {$prolog_stmt::append=true;})? DOT
		{$prolog_stmt::strings.add($prolog_stmt::temp);}
	-> ^(PRSO<Tuple>[$prolog_stmt.start, actions.castExprs($prolog_stmt::exprs), $expr::ctype, $prolog_stmt::strings, $prolog_stmt::append, false,""]))
	|  (PRO_SELECT {$prolog_stmt::strings.add($PRO_SELECT.text);} NAME{$prolog_stmt::strings.add($NAME.text);} 
	-> ^(PRO_SELECT<Tuple>[$prolog_stmt.start, actions.castExprs($prolog_stmt::exprs), $expr::ctype, $prolog_stmt::strings, $prolog_stmt::append, false,""]))
	)
	;
	
prologinsert
	: prologqueryfragment (PRIMP {$prolog_stmt::temp+=":-";} 
	prologqueryfragment (s2=COMMA {$prolog_stmt::temp+=$s2.text;}
	prologqueryfragment)*)?
	;


prologload
	: 	s = prologloadfragment {$prolog_stmt::temp+=$s.text;}
	|	prologexpr
	;
	
prologloadfragment
	:	(DIGITS)* NAME DOT NAME	
	;
	
prologquery
	:	prologqueryfragment
	;
	
prologqueryfragment
	:	prologatom
		(LPAREN {$prolog_stmt::temp+="(";}
		prologqueryinterior (s2=COMMA {$prolog_stmt::temp+=$s2.text;}
		prologqueryinterior)* 
		RPAREN {$prolog_stmt::temp+=")";})? 
	;
	
prologqueryinterior
	:	s3=STRING {$prolog_stmt::temp+=$s3.text;}
	|	prologexpr 
	;
	
prologatom
	:	e = atom
	{$prolog_stmt::exprs.add(actions.castExpr($e.tree));
	$prolog_stmt::strings.add($prolog_stmt::temp);
	$prolog_stmt::temp=""; }	
	;
	
prologsave
	: prologload
	| s1=CLEAR {$prolog_stmt::temp+=$s1.text;}
	;
	
prologexpr
	:	e = expr[expr_contextType.Load] 
	{$prolog_stmt::exprs.add(actions.castExpr($e.tree));
	$prolog_stmt::strings.add($prolog_stmt::temp);
	$prolog_stmt::temp=""; }	
	;
//============================================================================
/** ASP Syntax:			  asp_load:  	    ASP ?[expr].
											ASP ?[expr]+.
						  asp_query: 		ASP ?-aspquery.
						  asp_blankquery:	ASP ?-.
						  asp_insert:		ASP ?->aspquery.
						  asp_save:			ASP ?>>[expr | CLEAR].
						  					ASP ?>>[expr | CLEAR]+.
						  What a grammar can look like:
						  aspquery:			aspvarlist
						  					aspvarlist :- aspvarlist
						  					:- aspvarlist
						  aspvarlist:		aspqueryvar (, aspqueryvar)*
						  					(atom)* !{ aspqueryvar ( (, aspqueryvar) or (: aspqueryvar))* } (atom)*
						  aspqueryvar:		Note: \( or \) means it actually is ( or )
						  					aspnot ( \(expr ((, expr) or (; expr))*\) )*
						  					aspnot<atom..atom>
						  					aspnot(==)aspnot
						  					aspnot(!=)aspnot
						  					aspnot(<>)aspnot
						  					aspnot(<)aspnot
						  					aspnot(>)aspnot
						  					aspnot(<=)aspnot
						  					aspnot(>=)aspnot
						  aspnot:			(not)* atom
	
	What some ASP Syntax means:
						p(1..3). => p(1). p(2). p(3).
						p(x;q;l) => p(x). p(q). p(l).
	
						  
	Replacements from
	normal ASP:				Original	|		New
								:-		|		:=
								{ }		|		!{ }
								==		|		(==)
								!=		|		(!=)
								<>		|		(<>)
								>		|		(>)
								<		|		(<)
								>=		|		(>=)
								<=		|		(<=)
						  */


asp_stmt
scope{
	String dir;
	Boolean append;
	List exprs;
	List strings;
	String temp;
	
}
@init{
	expr etype = null;
}
@after {
	if (etype != null) {
		$asp_stmt.tree = etype;
	}
}
	:
		{
		$asp_stmt::dir = "";
		$asp_stmt::append = false;
		$asp_stmt::exprs = new ArrayList<expr>();
		$asp_stmt::strings = new ArrayList<String>();
		$asp_stmt::temp = "";
	}
	(
	(ASP PRLO{$asp_stmt::strings.add($PRLO.text);} aspload RBRACK (PLUS {$asp_stmt::append=true;})? DOT
    	{$asp_stmt::strings.add($asp_stmt::temp);}
	-> ^(PRLO<Tuple>[$asp_stmt.start,actions.castExprs($asp_stmt::exprs), $expr::ctype, $asp_stmt::strings, $asp_stmt::append, true, $asp_stmt::dir])) |
	(ASP ASPBLANKQ{$asp_stmt::strings.add($ASPBLANKQ.text);}
	-> ^(ASPBLANKQ<Tuple>[$asp_stmt.start,actions.castExprs($asp_stmt::exprs), $expr::ctype, $asp_stmt::strings, $asp_stmt::append, true, $asp_stmt::dir])) |
	(ASP ASPPRINTDB{$asp_stmt::strings.add($ASPPRINTDB.text);}
	-> ^(ASPPRINTDB<Tuple>[$asp_stmt.start,actions.castExprs($asp_stmt::exprs), $expr::ctype, $asp_stmt::strings, $asp_stmt::append, true, $asp_stmt::dir])) |
	(ASP PRQO{$asp_stmt::strings.add($PRQO.text);} aspquery DOT
    	{$asp_stmt::strings.add($asp_stmt::temp+".");}
	-> ^(PRQO<Tuple>[$asp_stmt.start,actions.castExprs($asp_stmt::exprs), $expr::ctype, $asp_stmt::strings, $asp_stmt::append, true, $asp_stmt::dir])) |
	(ASP PRIO{$asp_stmt::strings.add($PRIO.text);} aspquery DOT
    	{$asp_stmt::strings.add($asp_stmt::temp+".");}
	-> ^(PRQO<Tuple>[$asp_stmt.start,actions.castExprs($asp_stmt::exprs), $expr::ctype, $asp_stmt::strings, $asp_stmt::append, true, $asp_stmt::dir])) |
	(ASP PRSO{$asp_stmt::strings.add($PRSO.text);} aspsave RBRACK (PLUS {$asp_stmt::append=true;})? DOT
		{$asp_stmt::strings.add($asp_stmt::temp);}
	-> ^(PRSO<Tuple>[$asp_stmt.start, actions.castExprs($asp_stmt::exprs), $expr::ctype, $asp_stmt::strings, $asp_stmt::append, true, $asp_stmt::dir])) |
	(ASP_SELECT (REG_FACT{$asp_stmt::strings.add("reg_fact");} | GROUP_FACT{$asp_stmt::strings.add("group_fact");}) NAME{$asp_stmt::strings.add($NAME.text);} 
	-> ^(ASP_SELECT<Tuple>[$asp_stmt.start, actions.castExprs($asp_stmt::exprs), $expr::ctype, $asp_stmt::strings, $asp_stmt::append, true, $asp_stmt::dir])) |
	(ASP_PATH {$asp_stmt::strings.add($ASP_PATH.text);} aspdir
	-> ^(ASP_PATH<Tuple>[$asp_stmt.start,actions.castExprs($asp_stmt::exprs), $expr::ctype, $asp_stmt::strings, $asp_stmt::append, true, $asp_stmt::dir])) 
	
	)
	;

aspatom
	:	e = atom
	{$asp_stmt::exprs.add(actions.castExpr($e.tree));
	$asp_stmt::strings.add($asp_stmt::temp);
	$asp_stmt::strings.add("@ASPREPLACESTRINGHERE@");
	$asp_stmt::temp=""; }	
	;


aspload
	: 	s = asploadfragment {$asp_stmt::temp+=$s.text;}
	|	aspexpr
	;
	
asploadfragment
	:	(DIGITS)* NAME DOT NAME	
	;
	


aspexpr
	:	e = expr[expr_contextType.Load] 
	{$asp_stmt::exprs.add(actions.castExpr($e.tree));
	$asp_stmt::strings.add($asp_stmt::temp);
	$asp_stmt::strings.add("@ASPREPLACESTRINGHERE@");
	$asp_stmt::temp=""; }	
	;
	
	
// expr	
// expr:-expr
// :-expr
aspquery:
	aspvarlist (s2=PRIMP {$asp_stmt::temp+=":-";} aspvarlist)?
	| PRIMP {$asp_stmt::strings.add(":-");} aspvarlist
	;


aspvarlist:
	aspqueryvar ((s2=COMMA {$asp_stmt::temp+=$s2.text;} aspqueryvar)*|(ASPLC {$asp_stmt::temp+="{";} aspqueryvar ((s2=COLON {$asp_stmt::temp+=$s2.text;} aspqueryvar)|(s2=COMMA {$asp_stmt::temp+=$s2.text;} aspqueryvar))* RCURLY {$asp_stmt::temp+="}";} (aspatom)?)?)
	|
	ASPLC {$asp_stmt::temp+="{";} aspqueryvar ((s2=COMMA {$asp_stmt::temp+=$s2.text;} aspqueryvar)|(s2=COLON {$asp_stmt::temp+=$s2.text;} aspqueryvar))* RCURLY {$asp_stmt::temp+="}";} (aspatom)?
	;

aspqueryvar:
	aspnot
	(
	(LPAREN {$asp_stmt::temp+="(";}
	aspquerynotinterior ( (s2=COMMA {$asp_stmt::temp+=$s2.text;} aspquerynotinterior) | (SEMI {$asp_stmt::temp+="!@&@!";} aspquerynotinterior))*
	RPAREN {$asp_stmt::temp+=")";})
	|
	(LESS {$asp_stmt::temp+="(";} aspatom ASPDOTDOT {$asp_stmt::temp+="..";} aspatom GREATER {$asp_stmt::temp+=")";})
	|
	(LPAREN (EQUAL{$asp_stmt::temp+="==";} | NOTEQUAL{$asp_stmt::temp+="!=";} | ALT_NOTEQUAL{$asp_stmt::temp+="!=";} | LESS{$asp_stmt::temp+="<";} | GREATER{$asp_stmt::temp+=">";} | LESSEQUAL{$asp_stmt::temp+="<=";} | GREATEREQUAL{$asp_stmt::temp+=">=";}) RPAREN
	aspnot)
	)?
	;


	
aspquerynotinterior
	:	(NOT {$asp_stmt::temp+="not ";})* aspqueryinterior
	;
		
	
aspqueryinterior
	:	s3=STRING {$asp_stmt::temp+=$s3.text;}
	|	aspexpr 
	;
	
aspnot
	:
	(NOT {$asp_stmt::temp+="not ";})* aspatom
	;
	
aspsave
	: aspload
	| s1=CLEAR {$asp_stmt::temp+=$s1.text;}
	;

aspdir
	:	tempdir=path {$asp_stmt::dir += $tempdir.text + ";";} solverfrag?
	;
	
solverfrag
	:	SOLVER {$asp_stmt::strings.add($SOLVER.text);} tempsolver=path {$asp_stmt::dir += $tempsolver.text + ";";}
	;
//============================================================================	
//query_stmt: SELECT * FROM person WHERE x = value
sql_stmt
scope{
	List strings;
	List exprs;
	String temp;
}
scope connection;
@init {
    expr etype = null;
	$connection::url = "jdbc:oracle:thin:@rising-sun.microlab.cs.utexas.edu:1521:orcl";
	$connection::uname = "CS345_fjg344";
	$connection::pword = "orcl_fjg344";
	$connection::contype = "local";
}
@after {
    if (etype != null) {
        $sql_stmt.tree = etype;
    }
}
    :	 
    	{
           $sql_stmt::strings = new ArrayList<String>();
           $sql_stmt::exprs = new ArrayList<expr>();
           $sql_stmt::temp="";
      	} 
      	(	
		  (SELECT sqlquery SEMI {$sql_stmt::strings.add($sql_stmt::temp);  }
      	-> ^(SELECT<Tuple>[$sql_stmt.start, actions.castExprs($sql_stmt::exprs), $expr::ctype,$sql_stmt::strings, "SQL"]))
      	| (INSERT sqlinsert SEMI {$sql_stmt::strings.add($sql_stmt::temp);}
      	-> ^(INSERT<Tuple>[$sql_stmt.start, actions.castExprs($sql_stmt::exprs), $expr::ctype,$sql_stmt::strings, "SQL"]))
      	| (CREATE sqlcreate SEMI {$sql_stmt::strings.add($sql_stmt::temp);}
      	-> ^(CREATE<Tuple>[$sql_stmt.start, actions.castExprs($sql_stmt::exprs), $expr::ctype,$sql_stmt::strings, "SQL"]))
      	| (DROP sqldrop	 SEMI {$sql_stmt::strings.add($sql_stmt::temp);}
      	-> ^(DROP<Tuple>[$sql_stmt.start, actions.castExprs($sql_stmt::exprs), $expr::ctype,$sql_stmt::strings, "SQL"]))
      	| (UPDATE sqlupdate SEMI {$sql_stmt::strings.add($sql_stmt::temp);}
      	-> ^(UPDATE<Tuple>[$sql_stmt.start, actions.castExprs($sql_stmt::exprs), $expr::ctype,$sql_stmt::strings, "SQL"]))
      	| (SQL_DELETE sqldelete SEMI {$sql_stmt::strings.add($sql_stmt::temp);}
      	-> ^(SQL_DELETE<Tuple>[$sql_stmt.start, actions.castExprs($sql_stmt::exprs), $expr::ctype,$sql_stmt::strings, "SQL"]))
      	| (ALTER sqlalter SEMI {$sql_stmt::strings.add($sql_stmt::temp);}
      	-> ^(ALTER<Tuple>[$sql_stmt.start, actions.castExprs($sql_stmt::exprs), $expr::ctype,$sql_stmt::strings, "SQL"]))
	| (MAKECONNECT urlfrag SEMI
	-> ^(MAKECONNECT<Connection>[$sql_stmt.start, actions.castExprs($sql_stmt::exprs), $expr::ctype, $connection::url, $connection::uname, $connection::pword, $connection::contype]))
	| (ASPSELECT sqlquery SEMI {$sql_stmt::strings.add($sql_stmt::temp);  }
      	-> ^(ASPSELECT<Tuple>[$sql_stmt.start, actions.castExprs($sql_stmt::exprs), $expr::ctype, $sql_stmt::strings, "ASP"]))
      	| (RDFSELECT sqlquery SEMI {$sql_stmt::strings.add($sql_stmt::temp);  }
      	-> ^(RDFSELECT<Tuple>[$sql_stmt.start, actions.castExprs($sql_stmt::exprs), $expr::ctype, $sql_stmt::strings, "ASP"]))
      	
      	)
    ;
/*
sqlconnect
scope connection;
	:
	MAKECONNECT urlfrag namefrag pwordfrag contypefrag SEMI
	;
*/
urlfrag
	:
	tempurl=URLLINK {$connection::url=$tempurl.text.substring(4);} namefrag?
	;
	
namefrag
	:
	UNAME tempuname=NAME {$connection::uname=$tempuname.text;} pwordfrag?
	;

fragment pwordfrag
	:
	PWORD temppword=NAME {$connection::pword=$temppword.text;} contypefrag?
	;
	
contypefrag
	:
	CONTYPE tempcontype=NAME {$connection::contype=$tempcontype.text;}
	;	
	
sqlquery
    : s1=sqlqueryfrag {$sql_stmt::temp+=$s1.text+" ";}
	sqlwhereclause?
 	sqlorderbyclause?
    ;
	
sqlqueryfrag
	:  ('TOP')? ( STAR | (NAME DOT)? NAME (CAPSAS? NAME)? ( COMMA (NAME DOT)? NAME (CAPSAS? NAME)?)* | AGGREG (NAME DOT)? NAME RPAREN (CAPSAS NAME)? ) CAPSFROM (NAME CAPSAS?)? NAME ( COMMA (NAME CAPSAS?)? NAME)* (sqljoinfrag)? 
	;
	
sqljoinfrag
        : JOIN (NAME CAPSAS?)? NAME ON NAME DOT NAME ASSIGN NAME DOT NAME (JOIN (NAME CAPSAS?)? NAME ON NAME DOT NAME ASSIGN NAME DOT NAME)*
        ;

sqlorderbyclause
        : s2=sqlorderbyfrag {$sql_stmt::temp+=$s2.text+" ";}
        ;
sqlorderbyfrag
        : ORDER BY ( (NAME DOT)? NAME (ASCEND | DESCEND)? )+
        ;


sqlinsert
    :   s0a=INTO s0b=NAME {$sql_stmt::temp+=$s0a.text + " " + $s0b.text + " ";}
        ( s1=sqlinsertfrag {$sql_stmt::temp+=$s1.text+" ";})? sqlexpr
        ( s2=COMMA {$sql_stmt::temp+=$s2.text+" ";} sqlexpr )*
        ( s3=RPAREN {$sql_stmt::temp+=$s3.text+" ";} )?
    ;
sqlinsertfrag
        : LPAREN NAME ( COMMA NAME )* RPAREN VALUES LPAREN
        ;

sqlalter:	s1=sqlalterfrag {$sql_stmt::temp+=$s1.text+" ";}
	;
sqlalterfrag
	:TABLE NAME NAME  ('('|')'|','|NAME|FLOAT|INT)+	
	;		
sqlupdate
	: s1= sqlupdatefrag {$sql_stmt::temp+=$s1.text+" ";}  sqlexpr
	( s2=sqlsetfrag {$sql_stmt::temp+=$s2.text+" ";}   sqlexpr)* sqlwhereclause?	
	;
sqlupdatefrag
	: NAME SQL_SET sqlsetfrag
	;
sqlsetfrag
	: COMMA? NAME ASSIGN 	
	;
sqldelete
	:  s1=sqldeletefrag {$sql_stmt::temp+=$s1.text+" ";} sqlwhereclause?
	;
sqldeletefrag
	: CAPSFROM NAME
	;
sqldrop	
	: s1=sqldropfrag {$sql_stmt::temp+=$s1.text+" ";}	
	;

sqldropfrag
        : (TABLE (NAME DOT)? NAME (CASCADE CONSTRAINTS)? PURGE?) |
          (VIEW (NAME DOT)? NAME (CASCADE CONSTRAINTS)? PURGE?) |
          (INDEX (NAME DOT)? NAME FORCE?) |
          (FUNCTION (NAME DOT)? NAME) |
          (OPERATOR (NAME DOT)? NAME FORCE?) |
          (PROCEDURE (NAME DOT)? NAME) |
          (TRIGGER (NAME DOT)? NAME) |
          (TYPE (NAME DOT)? NAME (FORCE | VALIDATE)?)
        ;

sqlcreate
	: s1=sqlcreatefrag {$sql_stmt::temp+=$s1.text+" ";}	
	;
	
sqlcreatefrag
        : TABLE (NAME DOT)? NAME (LPAREN sqlrelationalproperties RPAREN)+
        ;

sqlrelationalproperties
        : sqlcolumndefinition
        ;

sqlcolumndefinition
        : NAME (NAME | INTTYPE | FLOATTYPE | CHARTYPE | DATETYPE) SORT? (DEFAULT sqlexpr)?
        ( COMMA NAME (NAME | INTTYPE | FLOATTYPE | CHARTYPE | DATETYPE) SORT? (DEFAULT sqlexpr)? )*
        ;

sqlcolumndefinition2
        : COMMA NAME (NAME | INTTYPE | FLOATTYPE | CHARTYPE | DATETYPE) SORT? (DEFAULT sqlexpr)?
        ;

sqlwhereclause
        : s2=sqlwherefrag1 {$sql_stmt::temp+=$s2.text+" ";} ( s4=sqlsubquery {$sql_stmt::temp+=$s4.text+" ";} | sqlexpr)
          ( s3=sqlwherefrag2 {$sql_stmt::temp+=$s3.text+" ";} sqlexpr )*
        ;

sqlwherefrag1
        : WHERE (NAME DOT)? NAME ( ASSIGN | LESS | LESSEQUAL | GREATER | GREATEREQUAL | ALT_NOTEQUAL )
        ;

sqlwherefrag2
	: ( CAPSAND | CAPSOR ) (NAME DOT)? NAME  ( ASSIGN | LESS | LESSEQUAL | GREATER | GREATEREQUAL | ALT_NOTEQUAL )
	;
	
sqlsubquery
	: LUNBAR SELECT sqlquery RUNBAR
	;

sqlexpr	//catches expressions and adds, also adding current string then reseting it
	: e = expr[expr_contextType.Load]
	{$sql_stmt::exprs.add(actions.castExpr($e.tree));$sql_stmt::strings.add($sql_stmt::temp);$sql_stmt::temp=""; }	
	;
	
sim_stmt
scope{
        List strings;
        List exprs;
        String temp;
}
scope connection;
@init {
    expr etype = null;
}
@after {
    if (etype != null) {
        $sim_stmt.tree = etype;
    }
}
    :
        {
           $sim_stmt::strings = new ArrayList<String>();
           $sim_stmt::exprs = new ArrayList<expr>();
           $sim_stmt::temp="";
        }
        (
	(MODIFY modifystmt SEMI {$sim_stmt::strings.add($sim_stmt::temp);}
        -> ^(MODIFY<Tuple>[$sim_stmt.start, actions.castExprs($sim_stmt::exprs), $expr::ctype, $sim_stmt::strings, "SIM"]))
	| (CAPSFROM retrievestmt {$sim_stmt::strings.add($sim_stmt::temp);}
        -> ^(FROM<Tuple>[$sim_stmt.start, actions.castExprs($sim_stmt::exprs), $expr::ctype, $sim_stmt::strings, "SIM"]))
	| (INSERT insertstmt SEMI {$sim_stmt::strings.add($sim_stmt::temp);}
        -> ^(FROM<Tuple>[$sim_stmt.start, actions.castExprs($sim_stmt::exprs), $expr::ctype, $sim_stmt::strings, "SIM"]))	
	| (CAPSCLASS class_stmt SEMI {$sim_stmt::strings.add($sim_stmt::temp);}
        -> ^(CAPSCLASS<Tuple>[$sim_stmt.start, actions.castExprs($sim_stmt::exprs), $expr::ctype, $sim_stmt::strings, "SIM"]))
	| (SUBCLASS subclass_stmt SEMI {$sim_stmt::strings.add($sim_stmt::temp);}
        -> ^(SUBCLASS<Tuple>[$sim_stmt.start, actions.castExprs($sim_stmt::exprs), $expr::ctype, $sim_stmt::strings, "SIM"]))	
)
   ;

fragment modifystmt
	:
	limitfrag? classfrag LPAREN assignment_expression (COMMA assignment_expression)* RPAREN whereclausefrag
	;

fragment retrievestmt
	:
	classfrag ret=RETRIEVE {$sim_stmt::strings.add($ret.text);} selectattributefrag (COMMA selectattributefrag)* fromwherefrag
	;

fragment insertstmt
	:
	classfrag (from_insert)? LPAREN assignment_expression (COMMA assignment_expression)* RPAREN
	;

fragment class_stmt
	:
	clname=NAME {$sim_stmt::strings.add($clname.text);} (comment_frag)? LPAREN (options {backtrack=true;} : dva_attr | eva_attr)* RPAREN
	;

fragment subclass_stmt
	:
	subclname=NAME {$sim_stmt::strings.add($subclname.text);} (comment_frag)? OF clname=NAME {$sim_stmt::strings.add("SUPERCLASS"); $sim_stmt::strings.add($clname.text);} LPAREN (options {backtrack=true;} : dva_attr | eva_attr)* RPAREN
	;

eva_attr
	:
	eva=NAME {$sim_stmt::strings.add("evaAttribute");$sim_stmt::strings.add($eva.text);} comment_frag? COLON clname=NAME {$sim_stmt::strings.add("targetClass");$sim_stmt::strings.add($clname.text);} ((COMMA)? {$sim_stmt::strings.add("EVAOPTIONS");} eva_options)? (COMMA eva_options)* SEMI
	;

dva_attr
	:
	dva=NAME {$sim_stmt::strings.add("dvaAttribute");$sim_stmt::strings.add($dva.text);} comment_frag? COLON data_type ((COMMA)? {$sim_stmt::strings.add("DVAOPTIONS");} dva_options)* SEMI
	;

comment_frag
	:
	comm=STRING {$sim_stmt::strings.add("COMMENT");$sim_stmt::strings.add($comm.text);}
	;

data_type
	:
 	dt=('INTEGERDATA'| 'STRINGDATA' | 'BOOLEANDATA'){$sim_stmt::strings.add("targetType");$sim_stmt::strings.add($dt.text);}
	;

dva_options
	:
	((REQD {$sim_stmt::strings.add("REQUIRED");}) | (INITVAL val=expr[expr_contextType.Load]{$sim_stmt::strings.add("INITIALVALUE"); $sim_stmt::exprs.add(actions.castExpr($val.tree));}))
	;

eva_options
	:
	((REQD {$sim_stmt::strings.add("REQUIRED");}) 
	| (SV {$sim_stmt::strings.add("SV");})
	| (MV {$sim_stmt::strings.add("MV");} (LPAREN {$sim_stmt::strings.add("MVOPTIONS");} eva_multivalued (COMMA eva_multivalued)* RPAREN {$sim_stmt::strings.add("MVOPTIONSEND");})?)
	| (INVERSE CAPSIS iname=NAME {$sim_stmt::strings.add("INVERSEIS"); $sim_stmt::strings.add($iname.text);} ))
	;

eva_multivalued
	:
	((DISTINCT {$sim_stmt::strings.add("DISTINCT");})| (MAXVAL mval=INT {$sim_stmt::strings.add("MAXVAL"); $sim_stmt::strings.add($mval.text);}))
	;

from_insert
	:
	fr=CAPSFROM {$sim_stmt::strings.add($fr.text);} classfrag whereclausefrag
	;

fromwherefrag
	:
        whr=WHERE
	((tname=NAME SEMI)|
        (atname=NAME ASSIGN val=expr[expr_contextType.Load] 
	{$sim_stmt::strings.add($whr.text); $sim_stmt::strings.add($atname.text);$sim_stmt::exprs.add(actions.castExpr($val.tree));}
        (CAPSAND atname=NAME  {$sim_stmt::strings.add($atname.text);} ASSIGN val=expr[expr_contextType.Load]  {$sim_stmt::exprs.add(actions.castExpr($val.tree));})* SEMI))
	;

selectattributefrag
	:
	dva=(NAME | STAR) {$sim_stmt::strings.add($dva.text);} ( evaconnector=OF eva=NAME {$sim_stmt::strings.add($evaconnector.text + " " + $eva.text);} ( evaconnector=OF eva=NAME {$sim_stmt::strings.add($evaconnector.text + " " + $eva.text);} )* )?	
	;

limitfrag
        :
	(lim=LIMIT ASSIGN e=expr[expr_contextType.Load]{$sim_stmt::strings.add($lim.text);$sim_stmt::exprs.add(actions.castExpr($e.tree));})
        ;

assignment_expression
	:
	 attributefrag (evafrag | dvafrag)
	;
classfrag
	:
	classname=NAME {$sim_stmt::strings.add($classname.text);}
	;

attributefrag
	:
        attname=NAME {$sim_stmt::strings.add("attributeToChange"); $sim_stmt::strings.add($attname.text);} PRIMP
	;

evafrag
	:
	( (in=INCLUDE {$sim_stmt::strings.add("evaValue"); $sim_stmt::strings.add($in.text);})? 
        evaValue=NAME {if ($in.text == null) {$sim_stmt::strings.add("evaValue");} $sim_stmt::strings.add($evaValue.text); } CAPSWITH LPAREN
        atname=NAME {$sim_stmt::strings.add($atname.text);} ASSIGN 
	val=expr[expr_contextType.Load] {$sim_stmt::exprs.add(actions.castExpr($val.tree));} 
        (CAPSAND atname=NAME  {$sim_stmt::strings.add($atname.text);} ASSIGN val=expr[expr_contextType.Load]  {$sim_stmt::exprs.add(actions.castExpr($val.tree));})* RPAREN 
	)
	;

dvafrag
	:
	(dvaValue=expr[expr_contextType.Load]{$sim_stmt::strings.add("dvaValue"); $sim_stmt::exprs.add(actions.castExpr($dvaValue.tree));})
	;


whereclausefrag
	:
	whr=WHERE {$sim_stmt::strings.add($whr.text);} 	
        atname=NAME {$sim_stmt::strings.add($atname.text);} ASSIGN 
	val=expr[expr_contextType.Load] {$sim_stmt::exprs.add(actions.castExpr($val.tree));} 
        (CAPSAND atname=NAME  {$sim_stmt::strings.add($atname.text);} ASSIGN val=expr[expr_contextType.Load]  {$sim_stmt::exprs.add(actions.castExpr($val.tree));})*
	;

sim_expr
	:
	expr[expr_contextType.Load]//{$sim_stmt::exprs.add(actions.castExpr($e.tree));}//$sim_stmt::strings.add($sim_stmt::temp);$sim_stmt::temp=""; }
	;
//=================
//===========================================================

sparql_stmt
scope{
        List strings;
        List exprs;
        String temp;
}
scope connection;
@init {
    expr etype = null;
}
@after {
    if (etype != null) {
        $sparql_stmt.tree = etype;
    }
}
    :
        {
           $sparql_stmt::strings = new ArrayList<String>();
           $sparql_stmt::exprs = new ArrayList<expr>();
           $sparql_stmt::temp="";
        }
        (
            (ENTAIL
            -> ^(ENTAIL<Tuple>[$sparql_stmt.start, null, $expr::ctype, $sparql_stmt::strings, "SPARQL"])))
;

//listmaker: test ( list_for | (',' test)* [','] )
listmaker[Token lbrack]
@init {
    List gens = new ArrayList();
    expr etype = null;
}
@after {
   $listmaker.tree = etype;
}
    : t+=test[$expr::ctype]
        (list_for[gens]
         {
             Collections.reverse(gens);
             List<comprehension> c = gens;
             etype = new ListComp($listmaker.start, actions.castExpr($t.get(0)), c);
         }
        | (options {greedy=true;}:COMMA t+=test[$expr::ctype])*
           {
               etype = new org.python.antlr.ast.List($lbrack, actions.castExprs($t), $expr::ctype);
           }
        ) (COMMA)?
    ;

//testlist_gexp: test ( gen_for | (',' test)* [','] )
testlist_gexp
@init {
    expr etype = null;
    List gens = new ArrayList();
}
@after {
    if (etype != null) {
        $testlist_gexp.tree = etype;
    }
}
    : t+=test[$expr::ctype]
        ( (options {k=2;}: c1=COMMA t+=test[$expr::ctype])* (c2=COMMA)?
         { $c1 != null || $c2 != null }? 
           {
               etype = new Tuple($testlist_gexp.start, actions.castExprs($t), $expr::ctype);
           }
        | -> test
        | (gen_for[gens]
           {
               Collections.reverse(gens);
               List<comprehension> c = gens;
               expr e = actions.castExpr($t.get(0));
               if (e instanceof Context) {
                   ((Context)e).setContext(expr_contextType.Load);
               }
               etype = new GeneratorExp($testlist_gexp.start, actions.castExpr($t.get(0)), c);
           }
          )
        )
    ;

//lambdef: 'lambda' [varargslist] ':' test
lambdef
@init {
    expr etype = null;
}
@after {
    $lambdef.tree = etype;
}
    : LAMBDA (varargslist)? COLON test[expr_contextType.Load]
      {
          arguments a = $varargslist.args;
          if (a == null) {
              a = new arguments($LAMBDA, new ArrayList<expr>(), null, null, new ArrayList<expr>());
          }
          etype = new Lambda($LAMBDA, a, actions.castExpr($test.tree));
      }
    ;

//trailer: '(' [arglist] ')' | '[' subscriptlist ']' | '.' NAME
trailer [Token begin, PythonTree ptree]
@init {
    expr etype = null;
}
@after {
    if (etype != null) {
        $trailer.tree = etype;
    }
}
    : LPAREN
      (arglist
       {
           etype = new Call($begin, actions.castExpr($ptree), actions.castExprs($arglist.args),
             actions.makeKeywords($arglist.keywords), $arglist.starargs, $arglist.kwargs);
       }
      |
       {
           etype = new Call($begin, actions.castExpr($ptree), new ArrayList<expr>(), new ArrayList<keyword>(), null, null);
       }
      )
      RPAREN
    | LBRACK subscriptlist[$begin] RBRACK
      {
          etype = new Subscript($begin, actions.castExpr($ptree), actions.castSlice($subscriptlist.tree), $expr::ctype);
      }
    | DOT attr
      {
          etype = new Attribute($begin, actions.castExpr($ptree), new Name($attr.tree, $attr.text, expr_contextType.Load), $expr::ctype);
      }
    ;

//subscriptlist: subscript (',' subscript)* [',']
subscriptlist[Token begin]
@init {
    slice sltype = null;
}
@after {
   $subscriptlist.tree = sltype;
}
    : sub+=subscript (options {greedy=true;}:c1=COMMA sub+=subscript)* (c2=COMMA)?
      {
          sltype = actions.makeSliceType($begin, $c1, $c2, $sub);
      }
    ;

//subscript: '.' '.' '.' | test | [test] ':' [test] [sliceop]
subscript
    returns [slice sltype]
@after {
    $subscript.tree = $sltype;
}
    : d1=DOT DOT DOT
      {
          $sltype = new Ellipsis($d1);
      }
    | (test[null] COLON)
   => lower=test[expr_contextType.Load] (c1=COLON (upper1=test[expr_contextType.Load])? (sliceop)?)?
      {
          $sltype = actions.makeSubscript($lower.tree, $c1, $upper1.tree, $sliceop.tree);
      }
    | (COLON)
   => c2=COLON (upper2=test[expr_contextType.Load])? (sliceop)?
      {
          $sltype = actions.makeSubscript(null, $c2, $upper2.tree, $sliceop.tree);
      }
    | test[expr_contextType.Load]
      {
          $sltype = new Index($test.start, actions.castExpr($test.tree));
      }
    ;

//sliceop: ':' [test]
sliceop
@init {
    expr etype = null;
}
@after {
    if (etype != null) {
        $sliceop.tree = etype;
    }
}
    : COLON
     (test[expr_contextType.Load]
    -> test
     |
       {
           etype = new Name($COLON, "None", expr_contextType.Load);
       }
     )
    ;

//exprlist: expr (',' expr)* [',']
exprlist
    [expr_contextType ctype] returns [expr etype]
    : (expr[null] COMMA) => e+=expr[ctype] (options {k=2;}: COMMA e+=expr[ctype])* (COMMA)?
       {
           $etype = new Tuple($exprlist.start, actions.castExprs($e), ctype);
       }
    | expr[ctype]
      {
        $etype = actions.castExpr($expr.tree);
      }
    ;

//not in CPython's Grammar file
//Needed as an exprlist that does not produce tuples for del_stmt.
del_list
    returns [List<expr> etypes]
    : e+=expr[expr_contextType.Del] (options {k=2;}: COMMA e+=expr[expr_contextType.Del])* (COMMA)?
      {
          $etypes = actions.makeDeleteList($e);
      }
    ;

//testlist: test (',' test)* [',']
testlist[expr_contextType ctype]
@init {
    expr etype = null;
}
@after {
    if (etype != null) {
        $testlist.tree = etype;
    }
}
    : (test[null] COMMA)
   => t+=test[ctype] (options {k=2;}: COMMA t+=test[ctype])* (COMMA)?
      {
          etype = new Tuple($testlist.start, actions.castExprs($t), ctype);
      }
    | test[ctype]
    ;

//dictmaker: test ':' test (',' test ':' test)* [',']
dictmaker
    returns [List keys, List values]
    : k+=test[expr_contextType.Load] COLON v+=test[expr_contextType.Load]
        (options {k=2;}:COMMA k+=test[expr_contextType.Load] COLON v+=test[expr_contextType.Load])*
        (COMMA)?
      {
          $keys = $k;
          $values= $v;
      }
    ;

//classdef: 'class' NAME ['(' [testlist] ')'] ':' suite
classdef
@init {
    stmt stype = null;
}
@after {
   $classdef.tree = stype;
}
    : decorators? CLASS NAME (LPAREN testlist[expr_contextType.Load]? RPAREN)? COLON suite[false]
      {
          Token t = $CLASS;
          if ($decorators.start != null) {
              t = $decorators.start;
          }
          stype = new ClassDef(t, actions.cantBeNoneName($NAME),
              actions.makeBases(actions.castExpr($testlist.tree)),
              actions.castStmts($suite.stypes),
              actions.castExprs($decorators.etypes));
      }
    ;

//arglist: (argument ',')* (argument [',']
//                         |'*' test (',' argument)* [',' '**' test]
//                         |'**' test)
arglist
    returns [List args, List keywords, expr starargs, expr kwargs]
@init {
    List arguments = new ArrayList();
    List kws = new ArrayList();
    List gens = new ArrayList();
}
    : argument[arguments, kws, gens, true, false] (COMMA argument[arguments, kws, gens, false, false])*
          (COMMA
              ( STAR s=test[expr_contextType.Load] (COMMA argument[arguments, kws, gens, false, true])* (COMMA DOUBLESTAR k=test[expr_contextType.Load])?
              | DOUBLESTAR k=test[expr_contextType.Load]
              )?
          )?
      {
          if (arguments.size() > 1 && gens.size() > 0) {
              actions.errorGenExpNotSoleArg(new PythonTree($arglist.start));
          }
          $args=arguments;
          $keywords=kws;
          $starargs=actions.castExpr($s.tree);
          $kwargs=actions.castExpr($k.tree);
      }
    | STAR s=test[expr_contextType.Load] (COMMA argument[arguments, kws, gens, false, true])* (COMMA DOUBLESTAR k=test[expr_contextType.Load])?
      {
          $starargs=actions.castExpr($s.tree);
          $keywords=kws;
          $kwargs=actions.castExpr($k.tree);
      }
    | DOUBLESTAR k=test[expr_contextType.Load]
      {
          $kwargs=actions.castExpr($k.tree);
      }
    ;

//argument: test [gen_for] | test '=' test  # Really [keyword '='] test
argument
    [List arguments, List kws, List gens, boolean first, boolean afterStar] returns [boolean genarg]
    : t1=test[expr_contextType.Load]
        ((ASSIGN t2=test[expr_contextType.Load])
          {
              expr newkey = actions.castExpr($t1.tree);
              //Loop through all current keys and fail on duplicate.
              for(Object o: $kws) {
                  List list = (List)o;
                  Object oldkey = list.get(0);
                  if (oldkey instanceof Name && newkey instanceof Name) {
                      if (((Name)oldkey).getId().equals(((Name)newkey).getId())) {
                          errorHandler.error("keyword arguments repeated", $t1.tree);
                      }
                  }
              }
              List<expr> exprs = new ArrayList<expr>();
              exprs.add(newkey);
              exprs.add(actions.castExpr($t2.tree));
              $kws.add(exprs);
          }
        | gen_for[$gens]
          {
              if (!first) {
                  actions.errorGenExpNotSoleArg($gen_for.tree);
              }
              $genarg = true;
              Collections.reverse($gens);
              List<comprehension> c = $gens;
              arguments.add(new GeneratorExp($t1.start, actions.castExpr($t1.tree), c));
          }
        |
          {
              if (kws.size() > 0) {
                  errorHandler.error("non-keyword arg after keyword arg", $t1.tree);
              } else if (afterStar) {
                  errorHandler.error("only named arguments may follow *expression", $t1.tree);
              }
              $arguments.add($t1.tree);
          }
        )
    ;

//list_iter: list_for | list_if
list_iter [List gens, List ifs]
    : list_for[gens]
    | list_if[gens, ifs]
    ;

//list_for: 'for' exprlist 'in' testlist_safe [list_iter]
list_for [List gens]
@init {
    List ifs = new ArrayList();
}
    : FOR exprlist[expr_contextType.Store] IN testlist[expr_contextType.Load] (list_iter[gens, ifs])?
      {
          Collections.reverse(ifs);
          gens.add(new comprehension($FOR, $exprlist.etype, actions.castExpr($testlist.tree), ifs));
      }
    ;

//list_if: 'if' test [list_iter]
list_if[List gens, List ifs]
    : IF test[expr_contextType.Load] (list_iter[gens, ifs])?
      {
        ifs.add(actions.castExpr($test.tree));
      }
    ;

//gen_iter: gen_for | gen_if
gen_iter [List gens, List ifs]
    : gen_for[gens]
    | gen_if[gens, ifs]
    ;

//gen_for: 'for' exprlist 'in' or_test [gen_iter]
gen_for [List gens]
@init {
    List ifs = new ArrayList();
}
    : FOR exprlist[expr_contextType.Store] IN or_test[expr_contextType.Load] gen_iter[gens, ifs]?
      {
          Collections.reverse(ifs);
          gens.add(new comprehension($FOR, $exprlist.etype, actions.castExpr($or_test.tree), ifs));
      }
    ;

//gen_if: 'if' old_test [gen_iter]
gen_if[List gens, List ifs]
    : IF test[expr_contextType.Load] gen_iter[gens, ifs]?
      {
        ifs.add(actions.castExpr($test.tree));
      }
    ;

//yield_expr: 'yield' [testlist]
yield_expr
    returns [expr etype]
@after {
    //needed for y2+=yield_expr
    $yield_expr.tree = $etype;
}
    : YIELD testlist[expr_contextType.Load]?
      {
          $etype = new Yield($YIELD, actions.castExpr($testlist.tree));
      }
    ;

//START OF LEXER RULES
AS        : 'as' ;
ASSERT    : 'assert' ;
BREAK     : 'break' ;
CLASS     : 'class' ;
CONTINUE  : 'continue' ;
DEF       : 'def' ;
DELETE    : 'del' ;
ELIF      : 'elif' ;
EXCEPT    : 'except' ;
EXEC      : 'exec' ;
FINALLY   : 'finally' ;
FROM      : 'from' ;
FOR       : 'for' ;
GLOBAL    : 'global' ;
IF        : 'if' ;
IMPORT    : 'import' ;
IN        : 'in' ;
IS        : 'is' ;
LAMBDA    : 'lambda' ;
ORELSE    : 'else' ;
PASS      : 'pass'  ;
PRINT     : 'print' ;
RAISE     : 'raise' ;
RETURN    : 'return' ;
TRY       : 'try' ;
WHILE     : 'while' ;
WITH      : 'with' ;
YIELD     : 'yield' ;

//*******lexer rules for prolog project.***************
CLEAR	:	'CLEAR'	;
PRO		: 	'PRO'	;
PRIMP	:	':='	;
PRIO	:	'?->'	;
PRLO	:	'?['	;
PRQO	:	'?-'	;
PRSO	:	'?>>['	;
PRO_SELECT: 'PRO_SELECT';
//*******end of lexer rules for prolog project.********

//*******lexer rules for asp***************
ASP			: 	'ASP'	;
ASPBLANKQ	:	'?-.'	;
ASPPRINTDB 	: 	'PRINT'	;
ASPLC		:	'!{'	;
ASPDOTDOT	:	'..'	;
REG_FACT	:	'?<<'	;
GROUP_FACT	:	'?@@'	;
ASP_SELECT	:	'ASP_SELECT'	;
ASP_PATH	:   'ASP_PATH'		;
SOLVER		:	'SOLVER'	;
//*******end of lexer rules for asp********

//*** begin lexer rules for SIM ***

LIMIT	: 'LIMIT' ;
CAPSWITH: 'WITH' ;
SV	:	'SV' | 'SINGLEVALUED';
MV	:	'MV' | 'MULTIVALUED';
INVERSE	:	'INVERSE';
CAPSIS	:	'IS';
DISTINCT:	'DISTINCT';
MAXVAL	:	'MAXVAL';
CAPSCLASS:	'CLASS';
SUBCLASS:	'SUBCLASS';
REQD	:	'REQUIRED';
INITVAL	:	'INITIALVALUE';
MODIFY	:	'MODIFY';
OF	:	'OF';
RETRIEVE:	'RETRIEVE';
INCLUDE :	'INCLUDE';
CTYPE   :	'CONNTYPE';

//*** end of lexer rules for SIM ***

//*** start of lexer rules for SPARQL ***
ENTAIL : 'ENTAIL';
//*** end of lexer rules for SPARQL ***

//====================================================================
//====================================================================

SELECT  : 	'SELECT' ;
CAPSFROM: 	'FROM' ;
WHERE   : 	'WHERE' ;
CAPSAND :	'AND' ;
CAPSOR  : 	'OR' ;
CAPSAS	:	'AS' ;
INSERT  : 	'INSERT' ;
INTO    : 	'INTO' ;
VALUES  : 	'VALUES' ;
CREATE	:	'CREATE';
TABLE	:	'TABLE';
VIEW	:	'VIEW';
INDEX	:	'INDEX';
ALTER	:	'ALTER';
DROP	:	'DROP';
UPDATE	:	'UPDATE';
SQL_DELETE:	'DELETE';
DEFAULT	:	'DEFAULT';
SORT	:	'SORT';
SQL_SET :	'SET';
CASCADE	:	'CASCADE';
CONSTRAINTS :	'CONSTRAINTS';
PURGE	:	'PURGE';
FUNCTION :	'FUNCTION';
OPERATOR :	'OPERATOR';
PROCEDURE :	'PROCEDURE';
TRIGGER	:	'TRIGGER';
TYPE	:	'TYPE';
FORCE	:	'FORCE';
VALIDATE :	'VALIDATE';
JOIN	:	'JOIN';
ON	:	'ON';
ORDER	:	'ORDER';
BY	:	'BY';
ASCEND	:	'ASC';
DESCEND	:	'DESC';
NULLS	:	'NULLS';
FIRST	:	'FIRST';
LAST	:	'LAST';
MAKECONNECT:	'MAKECONNECT';
URL	:	'URL';
UNAME	:	'UNAME';
PWORD	:	'PWORD';
CONTYPE  :	'CONTYPE';
AGGREG	:	'MAX('
	|	'MIN('
	|	'AVG('
	|	'COUNT('
	|	'FIRST('
	|	'LAST('
	|	'SUM('
	;
LUNBAR	:	'_|';
RUNBAR	:	'|_';
//new Tokens to help get ASP/Prolog facts 
ASPSELECT :	'ASPSELECT';
RDFSELECT :	'RDFSELECT';

INTTYPE	:	'BIT'
	|	'TINYINT'
	|	'BIGINT'
	;

FLOATTYPE :	'DECIMAL' ( LPAREN INT (COMMA INT)? RPAREN )?
	|	'NUMERIC' ( LPAREN INT (COMMA INT)? RPAREN )?
	|	'REAL'
	;

CHARTYPE :	'VARCHAR' LPAREN INT RPAREN
	|	'VARCHAR2' LPAREN INT RPAREN
	;
DATETYPE :	'DATE' //Use format 'DD-MMM-YY' for dates i.e. '13-NOV-92'
	;


//======================================================================
//======================================================================

LPAREN    : '(' {implicitLineJoiningLevel++;} ;

RPAREN    : ')' {implicitLineJoiningLevel--;} ;

LBRACK    : '[' {implicitLineJoiningLevel++;} ;

RBRACK    : ']' {implicitLineJoiningLevel--;} ;

COLON     : ':' ;

COMMA    : ',' ;

SEMI    : ';' ;

PLUS    : '+' ;

MINUS    : '-' ;

STAR    : '*' ;

SLASH    : '/' ;

VBAR    : '|' ;

AMPER    : '&' ;

LESS    : '<' ;

GREATER    : '>' ;

ASSIGN    : '=' ;

PERCENT    : '%' ;

BACKQUOTE    : '`' ;

LCURLY    : '{' {implicitLineJoiningLevel++;} ;

RCURLY    : '}' {implicitLineJoiningLevel--;} ;

CIRCUMFLEX    : '^' ;

TILDE    : '~' ;

EQUAL    : '==' ;

NOTEQUAL    : '!=' ;

ALT_NOTEQUAL: '<>' ;

LESSEQUAL    : '<=' ;

LEFTSHIFT    : '<<' ;

GREATEREQUAL    : '>=' ;

RIGHTSHIFT    : '>>' ;

PLUSEQUAL    : '+=' ;

MINUSEQUAL    : '-=' ;

DOUBLESTAR    : '**' ;

STAREQUAL    : '*=' ;

DOUBLESLASH    : '//' ;

SLASHEQUAL    : '/=' ;

VBAREQUAL    : '|=' ;

PERCENTEQUAL    : '%=' ;

AMPEREQUAL    : '&=' ;

CIRCUMFLEXEQUAL    : '^=' ;

LEFTSHIFTEQUAL    : '<<=' ;

RIGHTSHIFTEQUAL    : '>>=' ;

DOUBLESTAREQUAL    : '**=' ;

DOUBLESLASHEQUAL    : '//=' ;

DOT : '.' ;

AT : '@' ;

AND : 'and' ;

OR : 'or' ;

NOT : 'not' ;

FLOAT
    :   '.' DIGITS (Exponent)?
    |   DIGITS '.' Exponent
    |   DIGITS ('.' (DIGITS (Exponent)?)? | Exponent)
    ;

LONGINT
    :   INT ('l'|'L')
    ;

fragment
Exponent
    :    ('e' | 'E') ( '+' | '-' )? DIGITS
    ;

INT :   // Hex
        '0' ('x' | 'X') ( '0' .. '9' | 'a' .. 'f' | 'A' .. 'F' )+
    |   // Octal
        '0' ('o' | 'O') ( '0' .. '7' )*
    |   '0'  ( '0' .. '7' )*
    |   // Binary
        '0' ('b' | 'B') ( '0' .. '1' )*
    |   // Decimal
        '1'..'9' DIGITS*
;

COMPLEX
    :   DIGITS+ ('j'|'J')
    |   FLOAT ('j'|'J')
    ;

fragment
DIGITS : ( '0' .. '9' )+ ;

NAME:    ( 'a' .. 'z' | 'A' .. 'Z' | '_')
        ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '0' .. '9')* 
    ;

URLLINK: URL ' ' ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '0' .. '9' | COLON | AT | MINUS | DOT )+
    ;

/** Match various string types.  Note that greedy=false implies '''
 *  should make us exit loop not continue.
 */
STRING
    :   ('r'|'u'|'b'|'ur'|'R'|'U'|'B'|'UR'|'uR'|'Ur')?
        (   '\'\'\'' (options {greedy=false;}:TRIAPOS)* '\'\'\''
        |   '"""' (options {greedy=false;}:TRIQUOTE)* '"""'
        |   '"' (ESC|~('\\'|'\n'|'"'))* '"'
        |   '\'' (ESC|~('\\'|'\n'|'\''))* '\''
        ) {
           if (state.tokenStartLine != input.getLine()) {
               state.tokenStartLine = input.getLine();
               state.tokenStartCharPositionInLine = -2;
           }
        }
    ;

/** the two '"'? cause a warning -- is there a way to avoid that? */
fragment
TRIQUOTE
    : '"'? '"'? (ESC|~('\\'|'"'))+
    ;

/** the two '\''? cause a warning -- is there a way to avoid that? */
fragment
TRIAPOS
    : '\''? '\''? (ESC|~('\\'|'\''))+
    ;

fragment
ESC
    :    '\\' .
    ;

/** Consume a newline and any whitespace at start of next line
 *  unless the next line contains only white space, in that case
 *  emit a newline.
 */
CONTINUED_LINE
    :    '\\' ('\r')? '\n' (' '|'\t')*  { $channel=HIDDEN; }
         ( COMMENT
         | nl=NEWLINE
           {
               emit(new CommonToken(NEWLINE,nl.getText()));
           }
         |
         ) {
               if (input.LA(1) == -1) {
                   throw new ParseException("unexpected character after line continuation character");
               }
           }
    ;

/** Treat a sequence of blank lines as a single blank line.  If
 *  nested within a (..), {..}, or [..], then ignore newlines.
 *  If the first newline starts in column one, they are to be ignored.
 *
 *  Frank Wierzbicki added: Also ignore FORMFEEDS (\u000C).
 */
NEWLINE
@init {
    int newlines = 0;
}
    :   (('\u000C')?('\r')? '\n' {newlines++; } )+ {
         if ( startPos==0 || implicitLineJoiningLevel>0 )
            $channel=HIDDEN;
        }
    ;

WS  :    {startPos>0}?=> (' '|'\t'|'\u000C')+ {$channel=HIDDEN;}
    ;

/** Grab everything before a real symbol.  Then if newline, kill it
 *  as this is a blank line.  If whitespace followed by comment, kill it
 *  as it's a comment on a line by itself.
 *
 *  Ignore leading whitespace when nested in [..], (..), {..}.
 */
LEADING_WS
@init {
    int spaces = 0;
    int newlines = 0;
}
    :   {startPos==0}?=>
        (   {implicitLineJoiningLevel>0}? ( ' ' | '\t' )+ {$channel=HIDDEN;}
        |    (     ' '  { spaces++; }
             |    '\t' { spaces += 8; spaces -= (spaces \% 8); }
             )+
             ( ('\r')? '\n' {newlines++; }
             )* {
                   if (input.LA(1) != -1 || newlines == 0) {
                       // make a string of n spaces where n is column number - 1
                       char[] indentation = new char[spaces];
                       for (int i=0; i<spaces; i++) {
                           indentation[i] = ' ';
                       }
                       CommonToken c = new CommonToken(LEADING_WS,new String(indentation));
                       c.setLine(input.getLine());
                       c.setCharPositionInLine(input.getCharPositionInLine());
                       c.setStartIndex(input.index() - 1);
                       c.setStopIndex(input.index() - 1);
                       emit(c);
                       // kill trailing newline if present and then ignore
                       if (newlines != 0) {
                           if (state.token!=null) {
                               state.token.setChannel(HIDDEN);
                           } else {
                               $channel=HIDDEN;
                           }
                       }
                   } else if (this.single && newlines == 1) {
                       // This is here for this case in interactive mode:
                       //
                       // def foo():
                       //   print 1
                       //   <spaces but no code>
                       //
                       // The above would complete in interactive mode instead
                       // of giving ... to wait for more input.
                       //
                       throw new ParseException("Trailing space in single mode.");
                   } else {
                       // make a string of n newlines
                       char[] nls = new char[newlines];
                       for (int i=0; i<newlines; i++) {
                           nls[i] = '\n';
                       }
                       CommonToken c = new CommonToken(NEWLINE,new String(nls));
                       c.setLine(input.getLine());
                       c.setCharPositionInLine(input.getCharPositionInLine());
                       c.setStartIndex(input.index() - 1);
                       c.setStopIndex(input.index() - 1);
                       emit(c);
                   }
                }
        )
    ;

/** Comments not on line by themselves are turned into newlines.

    b = a # end of line comment

    or

    a = [1, # weird
         2]

    This rule is invoked directly by nextToken when the comment is in
    first column or when comment is on end of nonwhitespace line.

    Only match \n here if we didn't start on left edge; let NEWLINE return that.
    Kill if newlines if we live on a line by ourselves

    Consume any leading whitespace if it starts on left edge.
 */
COMMENT
@init {
    $channel=HIDDEN;
}
    :    {startPos==0}?=> (' '|'\t')* '#' (~'\n')* '\n'+
    |    '#' (~'\n')* // let NEWLINE handle \n unless char pos==0 for '#'
    ;
	
path : 
    ('/' NAME)+ {System.out.println("path is:" + $path.text);};
