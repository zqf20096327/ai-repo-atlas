# stems-arraign-48/neurocursor-ai

⭐ 40 · C++ · 推送 2026-08-20 · [GitHub](https://github.com/stems-arraign-48/neurocursor-ai) · [官网](https://neurocursor-ai.freedev.app/) · 个人维护

**用普通摄像头实现免手操鼠标光标控制的桌面应用**

C++ 编写的开源应用，将普通网络摄像头变为免手操作的指针设备：通过设备端轻量 AI 模型实时检测面部关键点并估计头部姿态与视线方向，经个性化校准映射、平滑滤波后注入操作系统光标位置，点击/拖拽/滚动由面部手势与停留时间触发。提供 Gaming 与 Everyday 两种档位、实时性能覆盖层与深度自定义设置，模型全部本地运行、无云端依赖，支持 Windows/macOS/Linux，从官网下载 zip 解压即用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 设备端实时面部关键点检测与头部姿态/视线估计，无云端依赖
- 约 30 秒的引导式逐用户校准流程
- 面部手势与 dwell 触发实现完全免手的点击/拖拽/滚动
- Gaming 与 Everyday 双档位及实时延迟/帧率性能覆盖层

## 适用场景

- 游戏中释放双手，用头部/视线控制相机或辅助瞄准轴
- 长时间浏览、办公时减少鼠标导致的重复劳损
- 手部活动受限用户的低成本指针替代方案
- 演示或直播中免手控制光标与幻灯片

## 场景标签

 · 领域:人机交互/计算机视觉辅助输入

## 证据(README 行号)

> L39: ### 🧠 Real-Time AI Face and Gaze Tracking
> L68: 2. **Facial Landmark Detection** — Each frame is passed through an AI model that identifies key facial landmarks, i

## 星数曲线

```mermaid
xychart-beta
    title "stems-arraign-48/neurocursor-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 39 --> 41
    line [40, 40]
```

2026-10-18 40 → 2026-10-28 40（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `4008a4f12c44` · [字段定义](../../DATASET.md)*
