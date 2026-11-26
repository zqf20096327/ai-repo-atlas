# Ilyas-Khiat/feed-brain

⭐ 3 · JavaScript · MIT · 推送 2026-11-23 · [GitHub](https://github.com/Ilyas-Khiat/feed-brain) · [官网](https://khiat.dev) · 个人维护

**个人知识库自动填充工具：把 YouTube/LinkedIn/X 内容转成 Obsidian 笔记**

由 Chrome 扩展、本地 Python 服务器和 Obsidian vault 组成的个人知识管理流水线：一键捕获 YouTube 视频或 LinkedIn/X 帖子，由 Claude（经 Claude Code CLI 无头运行）生成带时间戳、关键声明与可信度评级的笔记，写入共享概念笔记并构建主题图谱。内置 BM25F 全文检索、只读式问答（Ask the brain）与运行后校验机制。vault 为 git 仓库，支持多机同步，仅监听 127.0.0.1。依赖 Claude Code 登录订阅，用量计入其限额。

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

- 一键捕获：扩展点击或 Alt+Shift+Y，LinkedIn/X 收藏即触发
- Claude 生成笔记并联网核查声明，争议项加 ⚠ 标记与可信度评级
- Agentic 检索：无向量库，基于目录+BM25F+只读工具的多跳问答，逐点引用出处
- 运行后校验（超预算、无效链接、越界编辑）与工具白名单沙箱

## 适用场景

- 把看过的技术视频自动整理成可检索的 Obsidian 笔记
- 对自己的浏览/收藏历史用自然语言提问并追溯到原始出处
- 在多台电脑间通过 git 同步个人知识库

## 场景标签

`知识库管理` `知识图谱` · 领域:知识与检索

## 证据(README 行号)

> L4:  One click on a YouTube video, or a save or right-click on a LinkedIn or X post, and Claude turns it into a note you
> L27: |**2. Distill**|Claude writes a note sized to the video: a spoiler, 3 to 8 key claims each with an example and a ti
> L83: A capture is one headless `claude -p` run inside the vault folder, driven by an editable prompt (`server/prompt.md`


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `34ac13f15035` · [字段定义](../../DATASET.md)*
