# betizzel/rtx2070-super-tensor-unlock

⭐ 3 · Shell · MIT · 推送 2026-10-25 · [GitHub](https://github.com/betizzel/rtx2070-super-tensor-unlock) · 个人维护

**RTX 2070 SUPER 解锁满速 Tensor Core 的实测报告与脚本集**

记录在一张 RTX 2070 SUPER（TU104）上运行 nlzy/turing-unlock 的结果：FP16→FP32 tensor core 吞吐从半速率恢复到全速率，LLM prompt processing 达 1.76 倍提升。仓库提供测量数据、日志与工具脚本（固件生成、内核模块构建、单次启动 GRUB 条目、持久化安装与回退），并明确列出风险、单卡单机的局限与未验证项。不含固件或 exploit 代码，解锁本身来自上游项目。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- FP16→FP32 mma.sync 吞吐约 1.8–2 倍提升，FP32 累加正确性通过 CPU 参考校验
- LLM prompt 处理 241.7→426.3 tok/s（1.76×），decode 速率不变
- tools/ 提供从固件生成、单次启动试用到持久化安装的完整复现脚本
- 附 unlock-boot 日志分析、Xid 31 排查与 TU102/TU104 路径解释

## 适用场景

- 评估在 TU104 卡上尝试 turing-unlock 前的实测参考
- 复现满速 FP16→FP32 tensor core 解锁并跑基准对比
- 为 LLM 本地推理的 prompt 处理提速做硬件改造验证

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3: **First reported run of nlzy/turing-unlock on a TU104 card.**
> L9: This repository holds the measurements, logs and the small tools we used.

## 星数曲线

```mermaid
xychart-beta
    title "betizzel/rtx2070-super-tensor-unlock 星数(近 2 点)"
    x-axis ["2026-11-08", "2026-11-28"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-08 3 → 2026-11-28 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `f04e9f4bd502` · [字段定义](../../DATASET.md)*
