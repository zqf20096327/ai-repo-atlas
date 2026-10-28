# noemica-io/design-graph

⭐ 21 · HTML · MIT · 推送 2026-04-19 · [GitHub](https://github.com/noemica-io/design-graph) · [官网](https://noemica.io) · 组织维护

**给产品设计师/开发者：以流程图画布承载 AI 生成的界面变体**

无框架的单页 HTML 画布查看器：节点为磁盘上的自包含 HTML 页面，边为用户操作，同标签节点聚为变体簇，支持过滤、小地图、URL 状态回传与约 2 秒的 live-reload 轮询。生成侧随附 Claude Code skill（.claude/skills/design-graph-authoring/SKILL.md），教任意编码 agent 并行生成多个变体并即时写入 graph-data.js。项目按 data/{project}/ 目录组织，通过静态 HTTP 服务器运行；明确声明不绑定特定模型，Claude/GPT/Gemini/本地模型均可。MIT 许可，无账户无 SaaS。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单个 index.html 读取 graph-data.js + pages/*.html，无框架无构建
- 随附 Claude Code skill 教 agent 并行生成变体并即时写盘
- 项目级文件系统（data/{project}/）使一张画布容纳多个探索
- live-reload 约 2 秒将新节点上屏，拖拽位置在更新间保留

## 适用场景

- 让编码 agent 并行生成多个界面方向，在画布上对比筛选
- 以流程视角查看屏幕、用户动作与备选路径组成的产品体验
- 保留被淘汰的变体作为后续设计决策的上下文

## 场景标签

 · 领域:设计/原型工具

## 证据(README 行号)

> L46: - A bundled Claude Code skill that teaches any coding agent how to generate variants *correctly* — in parallel, wit
> L52: - Not tied to any model. Works with Claude, GPT, Gemini, local models — anything that can write HTML.
> L102: Design Graph is a viewer. The real work is generating pages, and it's meant to happen *in parallel*. The shipped s

## 星数曲线

```mermaid
xychart-beta
    title "noemica-io/design-graph 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `0777a74bbb63` · [字段定义](../../DATASET.md)*
