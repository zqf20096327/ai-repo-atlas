# daehyeonxyz/naite-personal-memory

⭐ 25 · Python · MIT · 推送 2026-09-23 · [GitHub](https://github.com/daehyeonxyz/naite-personal-memory) · 个人维护 · 中文 README

**由 LLM 维护的个人知识库：用 Claude Code/Codex 把资料长成互联 Markdown 树**

面向个人用户的知识库系统：将对话记录、讲义、论文等资料放入 vault，由 Claude Code 或 Codex 代理读取并整理为互相链接的 Markdown 知识页面（roots/tree 两层结构），以年龄段记录成长。全部为纯文本 Markdown，存于用户自己的 Git 仓库，无向量数据库，可用 Obsidian 打开查看图谱。提供 /naite 系列斜杠命令（grow/ask/fruit/care 等）与带图表视图的桌面应用，含防止个人信息提交的 Git 守护钩子；SOUL.md/USER.md/MEMORY.md 三个文件控制代理语气与记忆。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 代理自动将资料整理为互联 Markdown 知识页面，无需向量数据库
- 以 Claude Code 插件形式安装，也支持 Codex 直接复制仓库使用
- Windows/macOS/Linux 桌面应用，提供树状图谱视图与自动更新
- Git 守护钩子防止密钥与个人信息（USER.md/MEMORY.md）被提交

## 适用场景

- 沉淀与 AI 的日常对话和学习资料，形成个人知识树
- 换代理或跨会话后仍基于既有个人记录继续对话
- 将 ChatGPT/Claude/Gemini 导出的历史对话整理为知识页面
- 用 Obsidian 图谱视图浏览积累的知识关联

## 场景标签

`知识库管理` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L13: naite는 그 기록을 여러분의 것으로 만듭니다. 자료를 넣고 질문을 던지면 에이전트가 읽고 정리해서, 서로 연결된 지식 페이지로 쌓아 둡니다. 전부 평문 Markdown이라 어떤 서비스에도 묶이지 않고, 
> L39: 여러분이 할 일은 자료를 고르고 질문하는 것뿐입니다. 쓰고, 잇고, 다듬는 일은 에이전트의 몫입니다. 벡터 DB 같은 무거운 장치도 없습니다. 평문 Markdown이라 가볍고, Git으로 그대로 옮기거나 공

## 星数曲线

```mermaid
xychart-beta
    title "daehyeonxyz/naite-personal-memory 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-30 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `402cff58a83b` · [字段定义](../../DATASET.md)*
