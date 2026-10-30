# huggingface/jobs-actions

⭐ 16 · Python · NOASSERTION · 推送 2026-10-07 · [GitHub](https://github.com/huggingface/jobs-actions) · 组织维护

**在 Hugging Face Jobs 上运行 GitHub Actions 的桥接工具**

把 GitHub Actions 工作流转发到 Hugging Face Jobs 计算实例的桥接组件：修改 runs-on 标签（如 hf-jobs-a10g-small）即可将 CI 作业跑在 HF Jobs 的 CPU 或 GPU 机器上，GitHub Actions 仍负责编排、YAML、secrets 与 Checks UI，HF Jobs 提供算力。机制为 GitHub webhook 触发部署在 HF Space 的 Dispatcher，识别 hf-jobs-* 标签后调度作业。支持从 CPU 到 H200/RTX6000PRO 共 26 种规格标签，自称处于 Beta 阶段、接口可能变化。面向使用 GitHub CI 的开发团队，GPU 计费依赖 Hub 订阅。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 修改一行 runs-on 标签即可将 GitHub Actions 作业跑在 HF Jobs 上
- 支持 26 种运行规格标签，覆盖 CPU 与 T4/L4/A10G/A100/L40s/H200/RTX6000PRO 等 GPU
- GitHub 负责编排与 UI，HF Jobs 提供计算，无需自建 runner
- README 声明项目处于 Beta，可能发生变化

## 适用场景

- 为机器学习训练/评测流水线提供 GPU CI 算力
- 替代维护成本高的自托管 GitHub runner
- 在 PR 检查中直接使用多种 GPU 规格运行工作流

## 场景标签

 · 领域:开发工具/CI 基础设施

## 证据(README 行号)

> L3: Run your GitHub Actions workflows on **Hugging Face Jobs** with a one-line change:
> L18: Note that Jobs-Actions is in Beta, and could change. But the overall motivation for this is that GitHub-hosted runn

## 星数曲线

```mermaid
xychart-beta
    title "huggingface/jobs-actions 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-30"]
    y-axis "stars" 14 --> 17
    line [15, 16, 16]
```

2026-10-18 15 → 2026-10-30 16（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `96ba2d4123a6` · [字段定义](../../DATASET.md)*
