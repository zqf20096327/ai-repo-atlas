# ahujasid/mcp-for-blender

⭐ 31,534 · Python · MIT · 推送 2026-10-18 · [GitHub](https://github.com/ahujasid/mcp-for-blender) · [官网](https://www.mcp-for-blender.com/) · 个人维护

**让 AI 通过 MCP 协议控制 Blender 进行 3D 建模的社区插件**

由两部分组成：Blender 插件内建 socket 服务器接收并执行命令，以及实现 Model Context Protocol 的 Python 服务器连接两者。AI 可创建/修改/删除 3D 物体、控制材质、直接编写 Blender Python 代码，并通过多角度/线框/渲染视图自查结果。接入 Poly Haven、Sketchfab、Poly Pizza 资产及 Tripo、Hyper3D Rodin、Hunyuan3D 生成 3D 模型。提供一键安装脚本、pipx 与 Docker 运行方式；socket 服务器无认证加密，建议保持 localhost 或使用安全模式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`active` — 距上次 push 11.7 天,年发版 0,43 位贡献者
- 涨星:近 1 天 **+346**(自 20261016 起算)
- 平台:WINDOWS / MACOS / LINUX · 协议:MCP

## 能力要点

- 双向 socket 通信：AI 读写 Blender 对象、材质与场景
- 多角度/线框/X 光/渲染视图供 AI 自检成果
- 集成 Poly Haven、Sketchfab、Poly Pizza 与 Tripo/Hyper3D Rodin/Hunyuan3D 模型生成
- BLENDER_MCP_SAFE_MODE=1 可在执行前校验脚本并拦截风险代码

## 适用场景

- 用自然语言驱动 Blender 建模与场景搭建
- 让 AI 在 Blender 中生成或修改材质与物体
- 在对话式 AI 客户端中查看并操作 3D 视口

## 场景标签

 · 领域:3D 创作/AI 工具集成

## 证据(README 行号)

> L10: Prompt-assisted 3D modeling, scene creation, and manipulation — driven by AI.
> L132: 1. **Blender Addon** (`addon.py`) — a Blender addon that creates a socket server within Blender to receive and exe
> L133: 2. **MCP Server** (`src/blender_mcp/server.py`) — a Python server that implements the Model Context Protocol and c

---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `5aa412f59d09` · [字段定义](../../DATASET.md)*
