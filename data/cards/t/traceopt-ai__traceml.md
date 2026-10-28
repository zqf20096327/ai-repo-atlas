# traceopt-ai/traceml

⭐ 189 · Python · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/traceopt-ai/traceml) · [官网](https://traceopt.ai/) · 组织维护

**PyTorch 训练性能诊断工具：零代码定位慢训练瓶颈并在 CI 拦截性能回退**

通过 traceml run 命令包装既有训练脚本，自动对 Hugging Face Trainer、PyTorch Lightning、RF-DETR 的标准训练做插桩，按阶段（输入加载、H2D 传输、前向、反向、优化器）计时并输出瓶颈判定与证据（final_summary.json/txt）。提供 traceml compare 对比两次运行，可设步时回退阈值（如 5%）作为 CI 门禁返回退出码。支持单机 DDP 的 rank-straggler 诊断；多节点路径为实验性。自定义循环、Accelerate、Ray、DeepSpeed、MONAI 需显式集成 API。面向深度学习训练的开发者与 MLOps 场景，定位为轻量常开诊断，指向 GPU 计算内部时建议改用 kernel profiler。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 零代码插桩：traceml run 替换 python 即可诊断标准训练
- 六类瓶颈判定（Input/H2D/Compute/Residual/Rank straggler/Memory creep）
- traceml compare 支持 CI 性能回退门禁（可设回退百分比阈值）
- 单机 DDP 多 rank 对齐与 straggler 定位，可导出 HTML 报告并推送 W&B/MLflow

## 适用场景

- 训练变慢时定位是数据加载还是 GPU 计算瓶颈
- 改了 DataLoader/批大小后对比前后两次训练的性能差异
- 在 CI 中拦截导致步时回退的提交
- 排查多卡 DDP 训练中拖慢整体进度的 rank

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L26: TraceML shows where each training step goes—input loading, data transfer, forward, backward, and optimizer work—the
> L125: TraceML writes the evidence before returning the CI exit code. The regression

## 星数曲线

```mermaid
xychart-beta
    title "traceopt-ai/traceml 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 187 --> 190
    line [188, 189, 189]
```

2026-10-18 188 → 2026-10-28 189（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `34f814120258` · [字段定义](../../DATASET.md)*
