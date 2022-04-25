#include<iostream>
#include<vector>
#define ll long long
using namespace std;

int main(){

    vector<char> vec(63);

    for(ll i=0;i<63;i++)cin>>vec[i];
    //7*9
    vector<vector<char>> v79(7,vector<char> (9));
    vector<vector<char>> v97(9,vector<char> (7));

    vector<float> vv79(7,0),vv97(9,0);



    char t;    
    float ll79 = 9*0.4;
    float ll97 = 7*0.4;
    for(ll i=0;i<7;i++){
        for(ll j=0;j<9;j++){
            t=vec[i+j*7];
            // cout<<t<<" ";
            if(t == 'A' || t == 'E' || t == 'I' || t == 'O' || t == 'U') vv79[i]++;
        }
        vv79[i]= vv79[i]-ll79;
        if(vv79[i]<0)vv79[i]*=-1;
    }

    for(ll i=0;i<9;i++){
        for(ll j=0;j<7;j++){
            t=vec[i+j*9];
            if(t == 'A' || t == 'E' || t == 'I' || t == 'O' || t == 'U') vv97[i]++;

        }
        vv97[i]-=ll97;
        if(vv97[i]<0)vv97[i]*=-1;
    }
    
   
    
    for(ll i=1;i<7;i++)vv79[0]+=vv79[i];
    for(ll i=1;i<9;i++)vv97[0]+=vv97[i];
    
    cout<<"7*9's diff "<<vv79[0]<<endl<<"9*7's diff "<<" "<<vv97[0];

    return 0;
}