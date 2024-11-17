import { defineStore } from "pinia"
import axios from "axios";

export const useIssuesStore = defineStore
("issues", 
    {
        state:()=>({
            issues: [],
            loading: false,
            error: null,
        }),
        actions: {
            async fetchIssues(){
                try{
                    this.loading = true;
                    this.error = null;

                    const response = await axios.get("http://localhost:5000/api/consultas/"); //averiguar como hacer para que dependiendo el ambiente cambie la url
                    this.issues = response.data;
                    

                    //  [ 
                    //     {   id: 1, 
                    //         title: "Issue 1",
                    //         description: "Description of Issue 1",
                    //         user:{email: "user1@mail.com"},
                    //     },
                    //     {   id: 2, 
                    //         title: "Issue 2",
                    //         description: "Description of Issue 2",
                    //         user:{email: "juan@mail.com"},
                    //     },
                    //     {   id: 3, 
                    //         title: "Issue 3",
                    //         description: "Description of Issue 3",
                    //         user:{email: "sebastian@mail.com"},
                    //     },
                    // ]
                        
                    
                }
                catch{
                    this.error = "Error fetching issues"
                }
                finally{
                    this.loading = false
                }
            },
        },
    },
)