# Errata

Corrections are never edits. A correction is a **new** record appended to the chain that carries `supersedes` = the leaf of the record it replaces; the old row, its hashes and its timestamp proofs stay exactly as published. Readers take the latest record per date.

**2026-08-25 — stale-cache attestations.** Root cause: the attester read `/api/nav-history` through a stale-while-revalidate cache and, on some days, committed an intraday snapshot instead of the day's final one (drift ran in both directions; 20 up, 14 down; no net bias). Fixed the same day (fresh read + a completeness gate + a hard stop on any future drift). The affected days are re-attested below.

| date | nav (superseded) | nav (corrected) | red | supersedes leaf | erratum leaf | appended |
|---|---|---|---|---|---|---|
| 2026-03-22 | 6,249,837 | 6,186,074 | true→true | fe39ec2e3d91… | ecedfc75e72b… | 2026-08-25 |
| 2026-07-17 | 7,928,613 | 7,918,852 | true→true | 62132d4a8d4e… | c9069d481071… | 2026-08-25 |
| 2026-07-18 | 7,906,488 | 7,989,983 | true→false | 7b67967081c1… | b9674c4cbbf9… | 2026-08-25 |
| 2026-07-19 | 8,013,399 | 8,098,337 | false→false | 97d8667990ae… | e75e8816440e… | 2026-08-25 |
| 2026-07-20 | 8,076,101 | 8,181,271 | true→false | 8519b14f35f6… | 1edd0ba04c34… | 2026-08-25 |
| 2026-07-21 | 7,992,124 | 7,975,298 | true→true | c3415db74880… | 9e6ae3e78d32… | 2026-08-25 |
| 2026-07-22 | 7,917,837 | 7,952,126 | true→true | f6b9fe9d428c… | 052d16cf505e… | 2026-08-25 |
| 2026-07-23 | 7,755,908 | 7,761,894 | true→true | 134da9017aaf… | 322897866708… | 2026-08-25 |
| 2026-07-24 | 7,584,030 | 7,573,388 | true→true | 04ee51005312… | f056d828140c… | 2026-08-25 |
| 2026-07-25 | 7,646,721 | 7,640,813 | false→false | 43b43a4a801c… | d49162a07924… | 2026-08-25 |
| 2026-07-26 | 7,740,930 | 7,875,817 | false→false | 9f4e2749fd98… | 08fbab8e2c9f… | 2026-08-25 |
| 2026-07-27 | 7,870,143 | 7,643,966 | true→true | 71c5ddabf45b… | 03c21c4bc826… | 2026-08-25 |
| 2026-07-29 | 7,556,776 | 7,582,109 | true→false | 79c206d91d10… | c092c66fa0d5… | 2026-08-25 |
| 2026-08-02 | 7,524,977 | 7,561,944 | false→false | 7a9077e8dd8e… | 2a82fd3135ea… | 2026-08-25 |
| 2026-08-03 | 7,459,094 | 7,578,632 | true→false | 8ef30dcf53bb… | 446c656601bf… | 2026-08-25 |
| 2026-08-04 | 7,527,517 | 7,617,124 | true→false | 8454f55cef61… | ba65e68ba3a2… | 2026-08-25 |
| 2026-08-05 | 7,657,440 | 7,619,501 | false→false | 4a2b6ba3bc16… | 9d074f488e3f… | 2026-08-25 |
| 2026-08-06 | 7,516,650 | 7,503,915 | true→true | 61f3039c526c… | 879a4f378139… | 2026-08-25 |
| 2026-08-07 | 7,613,893 | 7,622,899 | false→false | 62d528ea5a58… | 30fd62414415… | 2026-08-25 |
| 2026-08-08 | 7,890,742 | 7,854,804 | false→false | 4b212fd037c6… | be30fcf1bfaf… | 2026-08-25 |
| 2026-08-09 | 8,024,906 | 7,958,684 | false→false | 5f2a362f8aaf… | 44cf09b664aa… | 2026-08-25 |
| 2026-08-10 | 7,893,746 | 7,908,527 | true→true | 31e9f514fa64… | b782ced21359… | 2026-08-25 |
| 2026-08-11 | 7,805,960 | 7,913,714 | true→false | 2f9d37c5e551… | 7375ae809bce… | 2026-08-25 |
| 2026-08-12 | 7,897,112 | 7,864,132 | true→true | e11bbc7c5bf8… | 1cf09a026797… | 2026-08-25 |
| 2026-08-13 | 7,811,881 | 7,860,157 | true→true | 296b40ae1163… | 7f1d0ddb5363… | 2026-08-25 |
| 2026-08-15 | 7,832,374 | 7,810,014 | false→false | 830b149957a8… | 778a84f909ec… | 2026-08-25 |
| 2026-08-16 | 7,799,497 | 7,730,092 | true→true | 271bd5c34709… | c34ea3042314… | 2026-08-25 |
| 2026-08-17 | 7,883,120 | 7,890,071 | false→false | e3b73b60425a… | fecc3ff169aa… | 2026-08-25 |
| 2026-08-18 | 8,015,867 | 8,023,556 | false→false | bf964e3833e6… | 310edf80fb18… | 2026-08-25 |
| 2026-08-19 | 8,907,633 | 8,892,442 | false→false | 8076a6eec769… | 4cc5983de97d… | 2026-08-25 |
| 2026-08-20 | 9,012,933 | 9,062,789 | false→false | e851381008f7… | 746c09589e70… | 2026-08-25 |
| 2026-08-21 | 9,012,880 | 9,258,822 | true→false | 417e6454ea9a… | 6f7957d24c30… | 2026-08-25 |
| 2026-08-23 | 9,210,833 | 9,372,459 | false→false | c0c11d6d13d1… | 81d0acb7c3e6… | 2026-08-25 |
| 2026-08-24 | 9,305,089 | 9,787,207 | true→false | f098c8e25fee… | ecc4a52e5afe… | 2026-08-25 |
