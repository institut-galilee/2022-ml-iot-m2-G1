//https://github.com/federicocotogno/accelerometer

package com.example.mwenweou

import android.hardware.Sensor
import android.hardware.SensorEvent
import android.hardware.SensorEventListener
import android.hardware.SensorManager
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import androidx.appcompat.app.AppCompatDelegate
import io.grpc.ManagedChannel
import io.grpc.ManagedChannelBuilder

class Hand : AppCompatActivity(), SensorEventListener {
    private lateinit var channel : ManagedChannel
    private lateinit var sensorManager: SensorManager

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_hand)

        AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_NO)
        setUpSensorStuff()
    }

    private fun setUpSensorStuff() {
        sensorManager = getSystemService(SENSOR_SERVICE) as SensorManager
        sensorManager.getDefaultSensor(Sensor.TYPE_ACCELEROMETER)?.also { accelerometer ->
            sensorManager.registerListener(
                this,
                accelerometer,
                SensorManager.SENSOR_DELAY_NORMAL,
                SensorManager.SENSOR_DELAY_NORMAL
            )
        }
    }

    override fun onSensorChanged(event: SensorEvent?) {
        if (event?.sensor?.type == Sensor.TYPE_ACCELEROMETER) {
            val sides = event.values[0]
            val upDown = event.values[1]
            val aboveunder = event.values[2]
            Log.e("SIDES", sides.toString())
            Log.e("UPDOWN", upDown.toString())
            Log.e("ABOVEUNDER", aboveunder.toString())

            channel = ManagedChannelBuilder.forAddress("10.100.26.12", 50051)
                .usePlaintext()
                .build()
            val stub : PredictorServiceGrpc.PredictorServiceBlockingStub = PredictorServiceGrpc.newBlockingStub(channel)

            val request : AccRequest = AccRequest.newBuilder().setSides( 5.8f ).setUpdown( 5.8f ).setAboveunder( 5.8f ).build()
            val reply : AccResponse = stub.predict(request)
        }
    }

    override fun onAccuracyChanged(sensor: Sensor?, accuracy: Int){
        return
    }

    override fun onDestroy(){
        sensorManager.unregisterListener(this)
        super.onDestroy()
    }
}