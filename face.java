package com.edu.hust.dangth.facedetection;

import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.graphics.RectF;
import android.graphics.drawable.BitmapDrawable;
import android.media.FaceDetector;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.SparseArray;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.Toast;

import com.google.android.gms.vision.Frame;
import com.google.android.gms.vision.face.Face;

public class MainActivity extends AppCompatActivity {

    ImageView image;
    Button button;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        image=(ImageView) findViewById(R.id.image);
        button=(Button) findViewById(R.id.process);

        final Bitmap myBitmap= BitmapFactory.decodeResource(getApplicationContext().getResources(),R.drawable.test);
        image.setImageBitmap(myBitmap);

        final Paint recPaint =new Paint();
        recPaint.setStrokeWidth(5);
        recPaint.setColor(Color.RED);
        recPaint.setStyle(Paint.Style.STROKE);

        final Bitmap tempBitmap= Bitmap.createBitmap(myBitmap.getWidth(),myBitmap.getHeight(),Bitmap.Config.RGB_565);
        final Canvas canvas=new Canvas(tempBitmap);
        canvas.drawBitmap(myBitmap,0,0,null);
        button.setOnClickListener( new View.OnClickListener(){

            @Override
            public void onClick(View view) {
                com.google.android.gms.vision.face.FaceDetector faceDetector =new com.google.android.gms.vision.face.FaceDetector.Builder(getApplicationContext()).setTrackingEnabled(false).setLandmarkType(com.google.android.gms.vision.face.FaceDetector.ALL_LANDMARKS).setMode(com.google.android.gms.vision.face.FaceDetector.FAST_MODE).build();
                if(!faceDetector.isOperational())
                {
                    Toast.makeText(MainActivity.this,"FaceDetector not be set up on your device",Toast.LENGTH_LONG).show();
                    return;
                }
                Frame frame= new Frame.Builder().setBitmap(myBitmap).build();
                SparseArray<Face> sparseArray =faceDetector.detect(frame);

                for(int i=0;i<sparseArray.size();i++)
                {
                    Face face =sparseArray.valueAt(i);
                    float x1=face.getPosition().x;
                    float y1=face.getPosition().y;
                    float x2=x1+face.getWidth();
                    float y2=y1+face.getHeight();
                    RectF rectF= new RectF(x1,y1,x2,y2);
                    canvas.drawRoundRect(rectF,2,2,recPaint);
                }
                image.setImageDrawable(new BitmapDrawable(getResources(),tempBitmap));
            }

        });
    }
}