# two-trick-pony-NL/PhotoScavenger

⭐ 15 · TypeScript · GPL-3.0 · 推送 2026-01-29 · [GitHub](https://github.com/two-trick-pony-NL/PhotoScavenger) · 个人维护

**拍照寻物对战手游：用图像识别判定照片是否含目标物体**

React Native 编写的多人拍照寻宝游戏：系统给出拍摄任务（如拍一个人、一株植物），玩家拍照后由 FastAPI 后端通过机器学习检测照片中的物体，命中则升级并获新任务，未命中则受罚，关卡难度随物体稀有度递增。同一代码库可编译 iOS 与 Android 应用，iOS 版已上架 App Store。物体检测由独立的后端仓库（PhotoScavenger2.0-Backend）承担。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 拍照任务式玩法：检测到目标物体即升级、未命中受罚
- 后端用机器学习检测照片中的物体（FastAPI + Python）
- React Native 跨平台，可编译 iOS 与 Android 应用

## 适用场景

- 与亲友对战比拼谁能先拍到指定物体
- 通过游戏化的拍照任务进行户外/室内活动

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L18: - When you open the app, you're given the assignment to photograph an object (e.g: 'a person')
> L26: - This app is supported by a FastAPI backend written in Python. It takes post requests with images and uses Machine

## 星数曲线

```mermaid
xychart-beta
    title "two-trick-pony-NL/PhotoScavenger 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `2d6271e0d69e` · [字段定义](../../DATASET.md)*
