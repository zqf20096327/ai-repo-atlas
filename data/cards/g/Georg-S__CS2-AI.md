# Georg-S/CS2-AI

⭐ 52 · C++ · BSD-3-Clause · 推送 2026-08-01 · [GitHub](https://github.com/Georg-S/CS2-AI) · 个人维护

**CS2 外部 AI 辅助工具：自瞄、扳机与自动移动**

面向 Counter-Strike 2 的外部程序，包含 aimbot、triggerbot 与自动移动三部分功能，基于 Qt6 构建，需 Visual Studio 2022 与 CMake 编译。自动移动功能依赖 navmesh，可通过该项目生成。程序读取游戏内存偏移（offsets.json、client_dll.json、buttons.json），偏移不定期更新，需从 cs2-dumper 项目下载新偏移文件覆盖配置目录。仓库未提供预编译二进制，仅给出源码构建流程。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 包含 aimbot、triggerbot 与自动移动功能
- 自动移动依赖 navmesh，navmesh 可由本项目生成
- 偏移文件从 cs2-dumper 下载更新，作者注明更新频率不高

## 适用场景

- 想为 CS2 编译运行 AI 辅助功能的使用者
- 需要生成 CS2 navmesh 用于自动移动的场景

## 场景标签

 · 领域:游戏/作弊工具

## 证据(README 行号)

> L3: An external CS2 AI consisting of an aimbot, triggerbot and automated movement.

## 星数曲线

```mermaid
xychart-beta
    title "Georg-S/CS2-AI 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-31"]
    y-axis "stars" 49 --> 53
    line [50, 52, 52]
```

2026-10-18 50 → 2026-10-31 52（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `0735966d38f6` · [字段定义](../../DATASET.md)*
