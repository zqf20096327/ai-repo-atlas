# PascalCorpsman/fpc_atomic

⭐ 60 · Pascal · NOASSERTION · 推送 2026-10-26 · [GitHub](https://github.com/PascalCorpsman/fpc_atomic) · 个人维护

**Atomic Bomberman 的可玩克隆：TCP 联网对战加机器人对手**

用 Free Pascal / Lazarus 重新实现的 1997 年 Atomic Bomberman 克隆。仓库只含源代码，图形与声音版权归 Interplay，玩家需自备原版 CD 并通过 atomic_launcher 提取素材后才能游玩。支持 TCP 网络多人对战、手柄（SDL2），自带自定义 AI 机器人（作者自述为不学习、不用神经网络的 agent），并提供 Free Pascal 与 C 模板供用户编写自己的 AI，可运行时加载。无单人模式，部分功能未实现。编译需自行安装 Lazarus IDE 及多个第三方单元。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 原版 TCP 联网对战的完整重实现（替代原 IPX）
- 附带 AI 机器人，并提供 FPC/C 模板编写自定义 AI，可运行时加载
- 提供 atomic_launcher 完成更新、CD 素材提取与启动
- 手柄支持（SDL2）

## 适用场景

- 拥有原版 Atomic Bomberman CD 的玩家进行怀旧联网对战
- 与 AI 机器人对战或编写自己的游戏 AI
- 研究经典游戏的开源重实现

## 场景标签

 · 领域:游戏/娱乐

## 证据(README 行号)

> L9: FPC Atomic is a complete reimplementation of the original Atomic Bomberman game (from 1997). This repository hosts o
> L43: - Custom AI implementation
> L92: The AI that is delivered with this repository is more a try than a real AI, and to be correct in words it's a agent

## 星数曲线

```mermaid
xychart-beta
    title "PascalCorpsman/fpc_atomic 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-25", "2026-10-28"]
    y-axis "stars" 57 --> 61
    line [58, 59, 60, 60]
```

2026-10-18 58 → 2026-10-28 60（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `8d12625abde1` · [字段定义](../../DATASET.md)*
