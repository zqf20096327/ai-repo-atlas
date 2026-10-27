# psu-efd/pyHMT2D

⭐ 134 · Python · MIT · 推送 2026-08-09 · [GitHub](https://github.com/psu-efd/pyHMT2D) · 组织维护

**Python 2D 水力建模控制与前后处理工具，支持 AI Agent 调用**

面向水力建模工程师的 Python 库，用于控制和半自动化 SRH-2D、HEC-RAS 2D 等模型：读取模拟结果到 Numpy 数组、转换为 VTK 可视化格式、修改模型参数、批量运行与校准，并提供 HEC-RAS 到 SRH-2D 的网格/边界条件互转。内置 MCP 服务器，将项目操作暴露为 AI agent 可调用工具，可配合 Claude Code、Cursor 等编程助手用自然语言完成建模流程，另提供 8 个 Agent Skills 与 JSON 参数的 hmt-cli 命令行。仅支持 Windows（受底层模型限制），需另行安装 SMS/SRH-2D 与 HEC-RAS。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 读取并转换 SRH-2D/HEC-RAS 结果为 VTK 格式，支持采样与探测
- 以脚本控制模型参数修改、批量运行、自动校准与 Monte-Carlo 模拟
- MCP 服务器暴露建模工具，供 MCP 兼容 AI 编程助手用自然语言调用
- 提供 /hmt-open、/hmt-run、/hmt-calibrate 等 8 个 Agent Skills 与 hmt-cli

## 适用场景

- 用 Python 脚本批量运行和校准 SRH-2D / HEC-RAS 2D 模型
- 在 AI 编程助手里用自然语言修改参数、跑模拟、查结果
- 将 2D 模拟结果转 VTK 可视化或转 3D 网格供 CFD 使用
- 在相同网格上对比 SRH-2D 与 HEC-RAS 2D 的结果差异

## 场景标签

 · 领域:工程计算/水力学

## 证据(README 行号)

> L5: *pyHMT2D* is a Python package for controlling and (semi)automating 2D hydraulic modeling, pre-/post-processing simul
> L61: - expose SRH-2D and HEC-RAS project operations through an MCP server with AI-agent-callable tools
> L62: - use natural-language prompts in MCP-capable AI coding assistants to inspect projects, edit Manning's n and bounda

## 星数曲线

```mermaid
xychart-beta
    title "psu-efd/pyHMT2D 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-27"]
    y-axis "stars" 132 --> 135
    line [133, 134, 134]
```

2026-10-18 133 → 2026-10-27 134（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `93cf95af7aa4` · [字段定义](../../DATASET.md)*
