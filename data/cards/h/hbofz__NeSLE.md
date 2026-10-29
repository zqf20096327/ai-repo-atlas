# hbofz/NeSLE

⭐ 35 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/hbofz/NeSLE) · [官网](https://github.com/hbofz/NeSLE/tree/main/docs) · 个人维护

**GPU 上的 NES 模拟器 RL 栈：单卡并行数千环境训练智能体**

将 NES 模拟（6502 CPU、PPU、总线、OAM DMA）整体实现在单个 CUDA kernel 中，每线程跑一台完整 NROM 主机，一次 kernel launch 步进数千个独立环境，观测驻留显存无需回传主机。提供 SB3 兼容的 NesleVecEnv 向量化环境、GPU 驻留的 PPO 实现（DLPack 与 PyTorch 交换张量）、超级马里奥兄弟奖励与 RAM 解析，以及八个世界的 FCEUX 存档快照重置与课程训练。限制：仅支持 Mapper 0 (NROM)；Windows 下 WDDM 驱动限制 PPO 吞吐；需自备合法 ROM。安装需 Python 3.10+、CUDA GPU、CUDA Toolkit 12.x 与 C++20 工具链，从源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单 CUDA kernel 内每线程模拟一台完整 NES，观测驻留设备内存
- GPU 驻留 PPO：rollout、GAE、优化器均在显存中运行
- 实现 SB3 VecEnv 契约（含 auto-reset），可接入现有 SB3 训练代码
- 八个世界 FCEUX 存档快照重置，支持 round-robin 课程训练

## 适用场景

- 在单块 GPU 上并行数千个超级马里奥兄弟环境做 PPO 训练
- 把现有 Stable-Baselines3 训练代码迁移到 GPU 向量化环境
- 复现 README 的性能与正确性检验结果

## 场景标签

`强化学习` · 领域:训练与推理

## 证据(README 行号)

> L5: NeSLE emulates the NES entirely inside a CUDA kernel: 6502 CPU, PPU, bus, and
> L9: SB3-compatible vectorized environment, a GPU-resident PPO implementation, and
> L26: - **GPU-resident PPO.** `nesle.native_ppo` keeps rollouts, GAE, and the

## 星数曲线

```mermaid
xychart-beta
    title "hbofz/NeSLE 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-29 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `cdc4cac1c2cf` · [字段定义](../../DATASET.md)*
