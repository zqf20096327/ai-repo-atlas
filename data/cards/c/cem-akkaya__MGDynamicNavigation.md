# cem-akkaya/MGDynamicNavigation

⭐ 19 · C++ · MIT · 推送 2025-12-15 · [GitHub](https://github.com/cem-akkaya/MGDynamicNavigation) · [官网](https://github.com/cem-akkaya/MGDynamicNavigation) · 个人维护

**UE5 插件：让 AI 在移动平台（船/电梯）上可靠寻路移动**

面向 Unreal Engine 5 的导航插件，解决 AI 角色在移动物体（船只、电梯、浮动岛、多甲板结构、物理驱动 Actor）上的移动问题。机制：烘焙阶段在体积内用射线检测 UE NavMesh 生成平台局部 3D 体素网格，运行时在局部坐标执行自定义 A* 求解生成路径点，再经球面检测修正生成随平台移动的样条线，AI 沿样条移动且不受平台旋转/物理影响。自带轻量避让与绕行点注入。自称为技术验证（TPOC），未实现与 UE 原生 NavMesh 之间的上下平台衔接，需项目自行扩展。

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

- 平台局部 3D 体素网格 + A* 寻路，不依赖运行时 NavMesh
- 样条随平台移动，不受旋转/物理模拟影响，支持多层甲板与坡道
- 球面检测的轻量避让与自动绕行
- Blueprint 与 C++ 均可调用，含网格可视化工具

## 适用场景

- 大型多甲板船只上的 AI 巡逻与移动
- 旋转或倾斜平台上的 AI 行走
- 物理驱动移动平台上让 AI 保持正确对位

## 场景标签

 · 领域:游戏开发/导航系统

## 证据(README 行号)

> L13: **MG Dynamic Navigation (MGDN)** is an Unreal Engine plugin that gives AI the ability to move reliably on **moving 
> L15: Instead of relying on the static Recast NavMesh, MGDN dynamically builds a **local 3D voxel navigation grid**, dete
> L86: 8. MGDN movement functions are available in C++ and Blueprint and uses dynamical pathfinding creating splines over 

## 星数曲线

```mermaid
xychart-beta
    title "cem-akkaya/MGDynamicNavigation 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `8cad88809cd9` · [字段定义](../../DATASET.md)*
