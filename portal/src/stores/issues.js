import { defineStore } from "pinia"

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
                    this.issues = 
                    [
                        {   id: 1, 
                            title: "Issue 1",
                            description: "Description of Issue 1",
                            user:{email: "user1@mail.com"},
                        },
                        {   id: 2, 
                            title: "Issue 2",
                            description: "Description of Issue 2",
                            user:{email: "juan@mail.com"},
                        },
                        {   id: 3, 
                            title: "Issue 3",
                            description: "Description of Issue 3",
                            user:{email: "sebastian@mail.com"},
                        },
                        
                    ]
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