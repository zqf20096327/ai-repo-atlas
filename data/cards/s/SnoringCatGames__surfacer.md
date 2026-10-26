# SnoringCatGames/surfacer

⭐ 118 · MIT · 推送 2026-10-13 · [GitHub](https://github.com/SnoringCatGames/surfacer) · [官网](https://snoringcat.games/play/squirrel-away) · 个人维护

**Godot 2D 平台游戏的寻路与角色移动框架**

面向 Godot 游戏开发者的 2D 平台游戏角色与寻路框架：提供客户端预测、感知表面的移动、跨平台寻路。原为 Godot 3 的 GDScript 实现（保存在 godot3 分支），正在以 Godot 4 + C++ GDExtension 重写（dev 分支），计划支持无需预解析静态平台图的动态寻路模式。当前 master 分支在重写期间仅保留 README，不含代码；稳定版需切换 godot3 分支获取。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 跨平台的 2D 寻路与感知表面的角色移动
- 客户端预测（client-side prediction）支持
- Godot 3 GDScript 稳定版与 Godot 4 C++ 重写版分分支维护

## 适用场景

- 2D 平台游戏角色移动与寻路开发
- 开发期通过 git 切换 dev/godot3 分支获取对应版本
- 为点击式或程序化平台关卡提供路径规划

## 场景标签

 · 领域:游戏开发

## 证据(README 行号)

> L6: A 2D platformer character / pathfinding framework for Godot
> L7: (client-side prediction, surface-aware movement, pathfinding across

## 星数曲线

```mermaid
xychart-beta
    title "SnoringCatGames/surfacer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 117 --> 119
    line [118, 118]
```

2026-10-18 118 → 2026-10-26 118（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `19c25fa26213` · [字段定义](../../DATASET.md)*
