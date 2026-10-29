# kanttouchthis/ComfyUI-SDNQ

⭐ 20 · Python · 推送 2026-01-06 · [GitHub](https://github.com/kanttouchthis/ComfyUI-SDNQ) · 个人维护

**为 ComfyUI 提供 SDNQ 量化支持的插件节点**

ComfyUI 的自定义节点扩展，将 SDNQ 量化能力接入 ComfyUI 工作流。SDNQ 本体并非直接提供，而是依赖作者自己的重新实现（含 HQQ 权重选择），通过 pip 从 GitHub 源码安装该依赖仓库。README 仅说明插件用途与依赖安装方式，附 Models 等章节，面向使用 ComfyUI 进行模型量化部署的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 为 ComfyUI 添加 SDNQ 量化支持
- 依赖作者实现的 SDNQ 版本，采用 HQQ 权重选择
- 依赖通过 pip 从 GitHub 源码安装

## 适用场景

- 在 ComfyUI 中使用 SDNQ 量化运行模型
- 对模型权重做 HQQ 选择式量化实验

## 场景标签

`模型量化` · 领域:训练与推理

## 证据(README 行号)

> L1: ## ComfyUI-SDNQ
> L2: SDNQ support for ComfyUI.
> L3: requires my own re-implementation of SDNQ with HQQ weight selection: `pip install git+https://github.com/kanttouchth

## 星数曲线

```mermaid
xychart-beta
    title "kanttouchthis/ComfyUI-SDNQ 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-29 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 low · 依据 README sha `ed74b08f1e66` · [字段定义](../../DATASET.md)*
