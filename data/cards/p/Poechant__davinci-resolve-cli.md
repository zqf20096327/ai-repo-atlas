# Poechant/davinci-resolve-cli

⭐ 53 · Python · MIT · 推送 2026-05-22 · [GitHub](https://github.com/Poechant/davinci-resolve-cli) · 个人维护

**操控 DaVinci Resolve 的 CLI/MCP 工具，供人与 AI agent 驱动剪辑流程**

以 Python 编写的命令行工具 dvr，通过 DaVinciResolveScript 桥接 DaVinci Resolve 18+，覆盖项目、媒体池、时间线、渲染队列与字幕的批量操作；输出 JSON/YAML/表格，错误以结构化 errorCode 返回。面向视频剪辑自动化用户与 AI agent：随 wheel 附带 SKILL.md 技能文件，并可启动暴露 20 个工具的 stdio MCP 服务器。限制：cut/move 依赖 Studio 版 Workflow Integration 插件，Free 版部分渲染编码器不可用；macOS 为主要验证平台。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- project/media/render/timeline/subtitle 五大命令域与异步渲染队列
- 内置 stdio MCP 服务器，暴露 20 个带 JSON-Schema 的工具
- 随包分发 SKILL.md，含 5 个示例 prompt
- 所有变更命令支持 --dry-run 与结构化错误码

## 适用场景

- 用终端批量导入素材、打标签、按日期分 bin
- 让 MCP 客户端的 AI agent 代为提交渲染并等待完成
- 从 CSV 批量添加章节标记，导入导出 srt/vtt 字幕

## 场景标签

`GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L12: A CLI for DaVinci Resolve 18+ — project / media / render / timeline control for humans and AI agents.
> L51: |`mcp`|—|Start a stdio MCP server exposing 20 tools (one per CLI verb), each with a JSON-Schema'd `inputSchema`|
> L86: ### 2. MCP server (`dvr mcp`)

## 星数曲线

```mermaid
xychart-beta
    title "Poechant/davinci-resolve-cli 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 52 --> 54
    line [53, 53]
```

2026-10-18 53 → 2026-10-24 53（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `b2e1550a8a7c` · [字段定义](../../DATASET.md)*
