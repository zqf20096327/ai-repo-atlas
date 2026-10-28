# ChiefGyk3D/FrankenLLM

⭐ 22 · Shell · NOASSERTION · 推送 2026-10-25 · [GitHub](https://github.com/ChiefGyk3D/FrankenLLM) · 个人维护

**多 NVIDIA GPU 各自跑独立 Ollama 模型的部署脚本套件**

面向 Ubuntu Server（24.04，测试于 Linux 6.14 + NVIDIA 580 驱动）的多 GPU LLM 服务部署工具：为每块 GPU 创建独立的 Ollama systemd 服务（各自端口如 11434/11435），实现按显存为每卡分配不同模型、开机自动预热、GPU 健康监测与驱动问题自动修复（最多重试 3 次重启）。提供交互式 Super Installer 与手动 configure/install 两套流程，支持 1 块以上 GPU、本地或 SSH 远程部署，可选安装 Open WebUI 网页界面与 RAG 数据集抓取脚本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每 GPU 独立 Ollama 实例（systemd 服务，分端口互不干扰）
- 开机自动预热模型与 GPU 健康监测/驱动自动修复
- 交互式安装向导，支持已有安装检测与重装选项
- 按显存档位（8/16/24/32GB+）给出模型选择与组合建议

## 适用场景

- 多张不同显存的 GPU 各自常驻不同 LLM 模型
- 搭建家用或远程的专用 LLM 推理服务器
- 配合 Open WebUI 建立带 RAG 嵌入模型的多模型 Web 界面

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L18: - 🚀 **Zero Interference** - Each GPU has its own Ollama instance on separate ports
> L70: - ✅ Ollama per-GPU services (with systemd)
> L124: - Creates systemd services for each GPU

## 星数曲线

```mermaid
xychart-beta
    title "ChiefGyk3D/FrankenLLM 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-28 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `9c0b5e00681f` · [字段定义](../../DATASET.md)*
