//quiz2
#include<iostream>
#include<vector>
#include<string>
#include<fstream>

#define ll long long

using namespace std;
int main(){
    
    while(1){    
        vector<ll> vec(26,0);
        char a;
        ll t=0;
        vector<float> f(26,0.0);
        //input use a '.' as ending
        while(cin>>a){
            if(a == '.')break;
            vec[a-48-17]++;
            if(a <= 'z' && a >='A')t++;

        }


        vector<ll> ic(26,0);
        for(ll i=0;i<26;i++){
            ic[i]=vec[i]*(vec[i]-1);
        }

        ll ttic=0;for(ll i=0;i<26;i++){
            ttic+=ic[i];
        }

        float ans = (float)ttic/(t*(t-1));
        // cout<<"ttic = "<<ttic<<endl;
        cout<<"==========================="<<endl;
        cout<<"ic = "<<ans<<endl;
        cout<<"==========================="<<endl;







    }



    



    return 0;
}