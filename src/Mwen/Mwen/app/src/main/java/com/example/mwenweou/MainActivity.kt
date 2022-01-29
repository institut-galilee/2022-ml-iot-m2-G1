package com.example.mwenweou

/**
 * @author Louise DAUDIN
 *
 * sources : https://developer.android.com/guide/topics/media/camera#manifest
 */
import android.R.id
import android.content.Context
import android.content.Intent
import android.os.Bundle
import android.view.View
import android.widget.Button
import androidx.appcompat.app.AppCompatActivity
import java.util.*


class MainActivity : AppCompatActivity() {


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
    }
    //Louise
    fun  toHand(view: View){
        val intent = Intent(this, Hand::class.java)
        startActivity(intent)
    }

    fun toHead(view : View){
        val intent = Intent(this, Head::class.java)
        startActivity(intent)
    }

    //finLouise


}