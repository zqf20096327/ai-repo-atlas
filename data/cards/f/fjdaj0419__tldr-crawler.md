# fjdaj0419/tldr-crawler

⭐ 3 · JavaScript · MIT · 推送 2026-11-19 · [GitHub](https://github.com/fjdaj0419/tldr-crawler) · 个人维护 · 中文 README

**Chrome 扩展：随阅读爬行网页并用 AI 生成分层 TL;DR 蛛网图谱**

零第三方依赖的 Chrome MV3 扩展，纯 JavaScript 编写。点击工具栏图标后，一只带程序化 IK 腿的蜘蛛从光标处爬向页面关键句并逐句高亮，句子批量发给 DeepSeek 或 Claude 生成中文短摘要，实时挂载到蛛网节点上；模型另读全文将其分组为块→主题→句子三层结构，点击节点可展开原句或跳转定位。无 API key 时蜘蛛仍可爬行高亮，但蛛网保持空置；AI 分组失败时回退到 HTML 标题或平面网。

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

- 蜘蛛跟随光标爬行并高亮关键句，AI 结果实时织入蛛网节点
- 分层结构：块→主题→句子，分组失败时回退 HTML h2–h4 标题或平面网
- 双引擎可选：DeepSeek 或 Anthropic Claude，选项页内置连接测试
- 零第三方依赖、无构建步骤，Manifest V3 + Shadow DOM 隔离

## 适用场景

- 快速提取长文章的分层要点，替代通读全文
- 阅读邮件、文档等文本嵌在 div 中的页面时提取要点
- 点击蛛网节点跳转回原句做定位精读

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L14: A Chrome extension written in plain JavaScript with **zero third-party dependencies**. Click the toolbar icon and a
> L42: - 🧠 **Dual engines** — DeepSeek or Anthropic Claude, switchable in the options page with a built-in connection test
> L88: No key is required to use the crawler: the spider still crawls and highlights, and the list keeps local summaries. 


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `715d07a350b7` · [字段定义](../../DATASET.md)*
