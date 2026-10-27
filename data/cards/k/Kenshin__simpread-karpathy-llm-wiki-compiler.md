# Kenshin/simpread-karpathy-llm-wiki-compiler

⭐ 34 · HTML · MIT · 推送 2026-06-12 · [GitHub](https://github.com/Kenshin/simpread-karpathy-llm-wiki-compiler) · [官网](https://simpread.pro) · 个人维护 · 中文 README

**把本地 Markdown 剪藏编译为个人结构化 Wiki 的 AI 协议方案**

简悦作者基于 Andrej Karpathy LLM Wiki 概念构建的个人知识库自动化方案：通过一套技能库（skills/）与命令（/gen、/ask、/report、/render 等）协议，让具备文件读写权限的 AI 环境（如 Claude Desktop/Code、Trae）将 raw/ 目录下的 Markdown 素材增量编译为带 Sources 溯源账本与双向链接的结构化 Wiki。2.0 版引入 index_map.txt 映射表实现增量感知；3.0 增加 Mermaid 知识图谱可视化（GraphLens）、HTML 排版系统与本地预览工具，另提供 MCP 工具集成实时检索简悦稍后读。目标受众为简悦资深用户与大量本地知识库的重度阅读者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- skills/ 技能库协议：初始化/添加/更新/审计/修复五类操作，增量处理 1000+ 行大文件
- index_map.txt 映射表实现增量感知，声称 Token 消耗降低 5-10 倍
- 每条 Wiki 知识挂载 Sources 账本与本地快照链接，原子级溯源
- MCP 工具集成实时检索简悦稍后读；GraphLens 知识图谱可视化与 lite/kami HTML 排版系统

## 适用场景

- 把稍后读囤积的文章自动编译成可溯源的个人维基
- 基于本地知识库做带来源链接的问答与简报生成
- 将 Wiki 条目渲染为 HTML 或交互式知识图谱分享阅读

## 场景标签

`知识库管理` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L14: 本项目是基于 **Andrej Karpathy** 提倡的 **LLM Wiki** 概念构建的 **个人知识库自动化知识构建方案**。它不仅是一套工具链，更是一种将 “被动囤积” 转化为 “主动内化” 的个人知识库自动化构建协
> L16: 这套框架利用具备文件读写权限的 AI 环境，将任意本地 Markdown 文件（或通过简悦导出的本地的本地快照）转化为高度结构化、可溯源、且具备双向链接的个人维基（Wiki），专为处理 **大规模（1000+）异步阅读素材** 而
> L241: 本项目 2.0 版本新增 **MCP (Model Context Protocol) 工具集成**，让你可以直接查询简悦本地快照库，实现实时、精准的内容检索。

## 星数曲线

```mermaid
xychart-beta
    title "Kenshin/simpread-karpathy-llm-wiki-compiler 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-27 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `f49a82982008` · [字段定义](../../DATASET.md)*
