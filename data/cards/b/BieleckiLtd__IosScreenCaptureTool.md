# BieleckiLtd/IosScreenCaptureTool

⭐ 15 · C# · MIT · 推送 2026-03-07 · [GitHub](https://github.com/BieleckiLtd/IosScreenCaptureTool) · 组织维护

**Windows 桌面工具：USB 镜像 iOS 屏幕并提供命令行截图**

基于 USB 将 iPhone/iPad 屏幕实时镜像到 Windows PC 的托盘应用（1–60 fps 可选），支持一键或命令行截图、自动重连、开机自启。底层依赖 pymobiledevice3 与 Apple USB 驱动（需安装 iTunes），iOS 16+ 需开启开发者模式，首次运行自动安装 Python 3.12 与 pymobiledevice3，启动需管理员权限。--capture-frame 与 --self-test 命令让 AI agent（如 Copilot、Claude）能读取设备画面帧，用于 UI 验证与 CI 视觉回归，但应用须先手动运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- USB 镜像 iOS 屏幕，1/5/25/30/60 fps 可调，无需设备端安装软件
- --capture-frame 单命令截图，供 AI agent 读取设备画面
- --self-test 一次性连接健康检查，可用于 CI 流程起点
- 托盘常驻、自动重连、可选开机自启

## 适用场景

- 在 Windows 上实时查看 iOS 设备屏幕并截图
- 让 AI agent 在合并 PR 前核验设备上的 UI 是否正确
- CI 中构建前后截图做视觉回归比对

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L9: - **See your iOS screen on your Windows PC** - live preview at up to 60 fps, just plug in the USB cable.
> L11: - **Let AI see your screen** - GitHub Copilot, Claude, Codex, or any automation can call one command to capture a f

## 星数曲线

```mermaid
xychart-beta
    title "BieleckiLtd/IosScreenCaptureTool 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `e4973ab88c84` · [字段定义](../../DATASET.md)*
