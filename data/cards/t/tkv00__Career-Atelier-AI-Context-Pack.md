# tkv00/Career-Atelier-AI-Context-Pack

⭐ 16 · JavaScript · MIT · 推送 2026-09-14 · [GitHub](https://github.com/tkv00/Career-Atelier-AI-Context-Pack) · [官网](https://tkv00.github.io/Career-Atelier-AI-Context-Pack/) · 个人维护

**个人自托管求职工作台：经验整理、AI 代写自荐信与面试准备**

面向求职者的个人安装型开源工作台（Next.js 网页 + 本地 Runner）。功能包括经验卡片与简历信息管理、导入 Markdown/PDF/Office/Notion 资料（本地 MarkItDown 转 Markdown）、招聘日程与结果跟踪、面试问题准备。AI 部分由 7 个角色化助手承担：企业调查、经验草稿、依据审查、小标题、岗位搜索、新闻、面试问题，通过用户订阅账户登录的 AI CLI（Codex/Claude Code/Antigravity）在本地执行。数据存于用户自己的 Supabase 项目，需 Node.js 22.13+ 与 Supabase CLI，npm start 一条命令启动网页与 Runner。限制：自动提交不支持，需全程人工确认。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 7 个角色助手覆盖企业调查→草稿→审查→小标题→面试题全流程
- 文件与 Notion 导入经本地 MarkItDown 转 Markdown，原比对后保存
- AI 经由 Codex / Claude Code / Antigravity CLI 以用户订阅账户运行，非 API 计费
- 数据存于个人 Supabase，`npm start` 一并启动网页与 Runner

## 适用场景

- 集中管理求职经验、简历与招聘日程
- 基于个人经验生成自荐信草稿并审查依据
- 生成公司专属面试题并组织答案
- 汇总现有 Notion / Office 文档以避免重复录入

## 场景标签

`知识库管理` `AI 写作` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L14: Career Atelier는 흩어진 경험·이력·채용공고를 모으고, 기업 조사부터 자소서 초안·검수·면접 준비까지 이어 주는 개인 취업 준비 작업실입니다.
> L103: 자소서 편집기에 **문항·글자 수·기업·직무·공고 내용**을 넣고 **기업 조사부터 소제목까지 실행 (솔)**을 선택합니다. 솔의 조사 → 뮤즈의 경험 기반 초안 → 렌즈의 근거·과장 검수 → 콤마의 소제
> L194: AI 기능을 쓰려면 AI CLI 하나 이상을 설치하고, **본인의 구독 계정**으로 로그인해야 합니다. 웹·러너 로그인과 AI CLI 로그인은 서로 별개입니다. 셋을 모두 설치할 필요는 없습니다.

## 星数曲线

```mermaid
xychart-beta
    title "tkv00/Career-Atelier-AI-Context-Pack 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `40530bcd548d` · [字段定义](../../DATASET.md)*
