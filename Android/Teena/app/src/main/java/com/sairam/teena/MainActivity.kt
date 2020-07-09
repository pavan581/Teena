package com.sairam.teena

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.text.Editable
import android.util.Log
import android.widget.Button
import android.widget.EditText
import android.widget.TextView

import com.chaquo.python.PyObject
import com.chaquo.python.Python
import com.chaquo.python.android.AndroidPlatform

class MainActivity : AppCompatActivity() {

    lateinit var textView: TextView
    lateinit var button: Button
    lateinit var editText: EditText

    lateinit var py: Python
    lateinit var pyf: PyObject

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        if (!Python.isStarted()) {
            Python.start(AndroidPlatform(this))
        }
        py = Python.getInstance()
        pyf = py.getModule("__init__")

        textView= findViewById(R.id.textview)
        button= findViewById(R.id.button)
        editText= findViewById(R.id.editTextView)

        var text = editText.text
        button.setOnClickListener { pyFun(text.toString()) }

    }

    private fun pyFun(text: String){
        Log.i("checktag","${text}")
        val obj: PyObject = pyf.callAttr("fun",text)
        textView.text = obj.toString()
    }
}