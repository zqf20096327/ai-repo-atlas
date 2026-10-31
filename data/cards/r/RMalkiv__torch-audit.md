# RMalkiv/torch-audit

⭐ 13 · Python · MIT · 推送 2026-01-24 · [GitHub](https://github.com/RMalkiv/torch-audit) · 个人维护

**PyTorch 训练循环的运行时审计库：检出静默训练缺陷**

面向 PyTorch 用户的运行时审计工具：在训练过程中检查真实张量、梯度、优化器配置与模型执行，检出 NaN/Inf 梯度、输入设备不匹配、可疑数值范围、僵尸层、Adam 误用 weight decay 等约 20 条内置规则（TA 系列编号，含严重级别与修复建议）。提供三种接入方式：monkey-patch 的 autopatch()、显式包装器、audit_step 装饰器；附 CLI 支持 CI 冒烟检查与基线过滤。注意 autopatch 与 torch.compile/TorchScript 不兼容。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 运行时检查真实张量/梯度/优化器配置，而非静态分析
- 约 20 条内置规则覆盖数据完整性、稳定性、优化配置、结构与性能提示
- autopatch()/包装器/装饰器三种接入模式
- CLI 支持规则列举与基线文件，可用于 CI 冒烟检查

## 适用场景

- 训练曲线异常时排查静默 bug（NaN 梯度、设备不匹配等）
- CI 中对模型做无训练循环的一次性审计
- 审查优化器配置常见错误（Adam+weight_decay、norm 参数误加正则）

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L12: Unlike a static linter, **torch-audit runs at runtime** and inspects what actually happens during training:
> L19: The goal is to catch **silent bugs** that don’t crash your code but quietly ruin training or waste compute.

## 星数曲线

```mermaid
xychart-beta
    title "RMalkiv/torch-audit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `0531f3c9671c` · [字段定义](../../DATASET.md)*
