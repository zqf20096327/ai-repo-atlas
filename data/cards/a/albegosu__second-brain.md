# albegosu/second-brain

⭐ 15 · Python · MIT · 推送 2026-10-13 · [GitHub](https://github.com/albegosu/second-brain) · 个人维护

**把 UI 灵感收藏自动整理为私有 wiki 与 DESIGN.md 的个人工具**

从手机或电脑分享 X/Instagram/LinkedIn 帖子、网页、截图或照片，由视觉模型读取画面、从像素测量配色并按 design/features/tools/practices 归档到私有 wiki 仓库；代码统计反复出现的选择生成 taste.md 与 DESIGN.md（经对比度检查的设计 tokens），并产出 AGENTS.md 供编码 agent 遵循。引擎以 git clone 加 bin/setup 安装，worker 默认跑在 GitHub Actions，也可本机或命令行运行；支持 Ollama/OpenAI/Anthropic/Gemini/OpenRouter 作为模型提供方，并附 Claude skill 与只读 MCP 服务器。已知限制：wiki 由模型撰写可能过度概括（每条声明指向逐字源笔记）、时序信息刻意省略、Instagram/LinkedIn 采集使用浏览器 cookie 违反平台条款。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 视觉模型从捕获画面提取特征与配色并按主题归档
- 自动生成 taste.md 与对比度检查、lint 清洁的 DESIGN.md tokens
- iPhone/Mac Shortcuts、Android 捕获页、命令行多端采集
- worker 默认运行于 GitHub Actions，无需依赖个人电脑；提供 Claude skill 与只读 MCP 服务器

## 适用场景

- 把刷到的界面设计灵感随手收藏并自动整理成个人设计知识库
- 将个人审美沉淀为 DESIGN.md 供编码 agent 设计时遵循
- 汇总自己常用的工具与实践成 stack.md 与 agent 规则

## 场景标签

`知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L3: **Save UI inspiration from any app. A vision model curates it into a private wiki
> L10: - **Curated, not dumped.** A vision model reads the frames, measures the palette

## 星数曲线

```mermaid
xychart-beta
    title "albegosu/second-brain 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `76a788f50c74` · [字段定义](../../DATASET.md)*
