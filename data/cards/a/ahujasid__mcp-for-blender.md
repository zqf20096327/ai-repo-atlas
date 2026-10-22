# ahujasid/mcp-for-blender

⭐ 31,861 · Python · MIT · 推送 2026-10-20 · [GitHub](https://github.com/ahujasid/mcp-for-blender) · [官网](https://www.mcp-for-blender.com/) · 个人维护

**让 LLM 通过 MCP 控制 Blender 做 3D 建模的插件**

由两部分组成：Blender 插件内置 socket 服务器接收并执行命令，以及实现 Model Context Protocol 的 Python 服务器连接二者。LLM 客户端（Claude Desktop/Code、Codex、Cursor、VS Code 等）可对 Blender 执行对象创建/修改/删除、材质控制、直接编写 Blender Python 代码，并可接入 Poly Haven、Sketchfab、Poly Pizza 资产及 Tripo、Hyper3D Rodin、Hunyuan3D 的 AI 生成 3D 模型；提供多角度视图与渲染让 AI 自检。要求 Blender 3.0+ 与 Python 3.10+，socket 服务器无认证与加密，另有可选安全模式校验脚本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`active` — 距上次 push 11.7 天,年发版 0,43 位贡献者
- 涨星:近 1 天 **+346**(自 20261016 起算)
- 安装:github 包 `release-assets` 月下载无数据
- 平台:WINDOWS / MACOS / LINUX · 协议:MCP

## 能力要点

- Blender 插件 + MCP 服务器双组件架构，支持多款 MCP 客户端接入
- 对象/材质操作与 AI 直接编写 Blender Python 代码
- Poly Haven、Sketchfab 资产接入及 Tripo、Hyper3D Rodin、Hunyuan3D 生成 3D 模型
- 可选安全模式（BLENDER_MCP_SAFE_MODE=1）校验并拦截高风险脚本

## 适用场景

- 用 Claude 等 AI 客户端对话式完成 Blender 建模与场景搭建
- 让 AI 生成 3D 模型并直接导入 Blender 场景
- 通过 AI 编写并执行 Blender Python 自动化脚本

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L117: |**Two-way communication**|Connect Claude AI to Blender through a socket-based server|
> L133: 2. **MCP Server** (`src/blender_mcp/server.py`) — a Python server that implements the Model Context Protocol and c

## 星数曲线

```mermaid
xychart-beta
    title "ahujasid/mcp-for-blender 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 31321 --> 31910
    line [31370, 31672, 31861]
```

2026-10-18 31,370 → 2026-10-22 31,861（+491）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-20 · 置信度 high · 依据 README sha `90a2a5c79439` · [字段定义](../../DATASET.md)*
