package com.example.luggagecarrier;

import androidx.fragment.app.FragmentActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.SupportMapFragment;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.MarkerOptions;

import java.util.Random;
import java.util.concurrent.TimeUnit;

public class MapsActivity extends FragmentActivity implements OnMapReadyCallback {

    private GoogleMap mMap;
    private double latCoordinate;
    private double lonCoordinate;
    private LatLng coordinate;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_maps);
        // Obtain the SupportMapFragment and get notified when the map is ready to be used.
        SupportMapFragment mapFragment = (SupportMapFragment) getSupportFragmentManager()
                .findFragmentById(R.id.map);
        mapFragment.getMapAsync(this);

        //type casting for btn
        Button newPoint = (Button) findViewById(R.id.btnNewPoint);
        newPoint.setOnClickListener(btnNewPointGenerator);
    }

    /**
     * Manipulates the map once available.
     * This callback is triggered when the map is ready to be used.
     * This is where we can add markers or lines, add listeners or move the camera.
     * If Google Play services is not installed on the device, the user will be prompted to install
     * it inside the SupportMapFragment. This method will only be triggered once the user has
     * installed Google Play services and returned to the app.
     */
    @Override
    public void onMapReady(GoogleMap googleMap) {
        mMap = googleMap;

        //generate coordinate
        double latCoordinate1 = getRandomNumberInRange(-90, 90);
        double lonCoordinate1 = getRandomNumberInRange(-180, 180);
        LatLng coordinate1 = new LatLng(latCoordinate1, lonCoordinate1);

        // Add a marker at new coordinate and move the camera
        mMap.addMarker(new MarkerOptions().position(coordinate1).title("Some device info could be here"));
        mMap.moveCamera(CameraUpdateFactory.newLatLng(coordinate1));

    }

    //on button click: clear map, generate new point, map it and move camera
    View.OnClickListener btnNewPointGenerator = new View.OnClickListener() {
        @Override
        public void onClick(View v) {
            //clear
            mMap.clear();

            //generate
            latCoordinate = getRandomNumberInRange(-90, 90);
            lonCoordinate = getRandomNumberInRange(-180, 180);
            coordinate = new LatLng(latCoordinate, lonCoordinate);

            //move
            mMap.addMarker(new MarkerOptions().position(coordinate).title("Some device info could be here"));
            mMap.moveCamera(CameraUpdateFactory.newLatLng(coordinate));
        }
    };

    //get random numbers
    private static double getRandomNumberInRange(double min, double max) {
        Random r = new Random();
        return min + (max - min) * r.nextDouble();
    }
}