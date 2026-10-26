# mprahboamey/atom

⭐ 57 · Python · MIT · 推送 2026-08-15 · [GitHub](https://github.com/mprahboamey/atom) · 个人维护

**用光学干涉精确计算 Transformer attention 分数的软件/系统基础**

探索性研究仓库：将 query/key 以二值相位(0/π)编码为波幅，通过干涉逐项恢复实内积，使分数矩阵与 QKᵀ/√d 恒等（有单元测试）。架构为混合式：光学路径算分数，数字路径处理 softmax、values、MLM 等。已在 SmolLM2-135M-Instruct 全部 30 层上用 safetensors 权重做贪心解码对比，日志显示 top-1 一致率 100%（限短序列）。物理光折变写入/读取回路为未来工作，仓库定位为软件与系统基础，含 FPGA 脚手架与容量/机架规划模块。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 二值相位编码下干涉结果与 scaled dot-product attention 恒等的机制声明，附单元测试
- 在 SmolLM2-135M-Instruct（30 层）上做混合推理与数字解码对比
- 提供 safetensors/GGUF 混合生成、容量模型、多晶体机架布局、FPGA 脚手架模块

## 适用场景

- 研究光学计算实现 attention 的机制与验证方法
- 在真实模型权重上运行光学分数的混合推理实验
- 为光学硬件实现做容量与刷新策略建模

## 场景标签

 · 领域:光学计算/机器学习系统

## 证据(README 行号)

> L5: Transformer **attention scores** from optical interference — with an exact
> L20: **Architecture:** optical (or optical-model) path computes scores; digital
> L42: |`atom/hybrid_model.py`|Safetensors / GGUF hybrid generate|

## 星数曲线

```mermaid
xychart-beta
    title "mprahboamey/atom 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 56 --> 58
    line [57, 57]
```

2026-10-18 57 → 2026-10-26 57（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `9e57ad5bd5df` · [字段定义](../../DATASET.md)*
