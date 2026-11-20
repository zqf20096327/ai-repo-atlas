# haowern98/ModelLoom

⭐ 11 · TypeScript · 推送 2026-11-09 · [GitHub](https://github.com/haowern98/ModelLoom) · 个人维护

**本地多机多 GPU 分发运行 GGUF 模型的 Windows 桌面应用**

ModelLoom 是一个 Windows 桌面应用，用于在单 GPU、单机多 GPU 或两台 PC 组成的私有网络集群上运行 GGUF 模型。用户在 GUI 中导入模型文件、在集群画布上按层分配 GPU 负载、内置聊天界面发送提示，并提供本地 OpenAI 兼容 API 供脚本和其他应用调用。首次启动时选择 CUDA 或 Vulkan 后端，应用会下载并校验对应的 llama.cpp 运行时；Residency Bridge 机制在重复张量写入时发送短引用以减少协调节点与工作节点间的网络流量。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 在集群画布上按设备卡直接指定模型层到 GPU 的分配范围
- 协调节点+工作节点两机私有网络分布式推理
- 内置聊天界面与本地 OpenAI 兼容 API
- Residency Bridge 对重复张量写入发送短引用以降低流量

## 适用场景

- 把一个大的 GGUF 模型分层拆到多张已有 GPU 上运行
- 用两台 PC 通过局域网分担模型推理负载
- 从脚本或第三方应用通过 OpenAI 兼容接口调用本地模型

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L19: ModelLoom is a Windows desktop app for running GGUF models on one GPU, splitting layers across multiple GPUs in one
> L40: - **Built-in Chat** — Send prompts to a loaded model from the desktop app.

## 星数曲线

```mermaid
xychart-beta
    title "haowern98/ModelLoom 星数(近 3 点)"
    x-axis ["2026-11-10", "2026-11-15", "2026-11-20"]
    y-axis "stars" 9 --> 12
    line [10, 11, 11]
```

2026-11-10 10 → 2026-11-20 11（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 high · 依据 README sha `211288f99653` · [字段定义](../../DATASET.md)*
