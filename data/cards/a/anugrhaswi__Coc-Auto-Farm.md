# anugrhaswi/Coc-Auto-Farm

⭐ 24 · Python · MIT · 推送 2026-10-22 · [GitHub](https://github.com/anugrhaswi/Coc-Auto-Farm) · 个人维护

**部落冲突自动刷资源机器人：YOLO+OCR 识别，ADB 后台挂机**

面向 Windows 模拟器（默认 LDPlayer）的部落冲突挂机工具：通过 ADB 截屏与点击实现后台运行（窗口可最小化），固定按钮采用一次校准的归一化坐标，动态内容（阵型、金币/圣水/暗黑重油数值、战利品）由 YOLO 与 EasyOCR 检测；资源达到阈值自动进攻。提供 Tkinter 线程安全 GUI、F12 停止、重试自恢复与 ntfy.sh 推送。限制：仅支持 ADB 单实例、仅哥布林单一策略、需自备 YOLO 模型 best.pt。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ADB 截屏/点击实现后台挂机，无需窗口焦点
- 固定按钮走校准坐标，游戏更新后重校准即可，无需重训 YOLO
- YOLO + EasyOCR 检测阵型与资源数值，按阈值自动进攻
- Tkinter 线程安全 GUI + ntfy.sh 错误/完成推送

## 适用场景

- 挂机自动刷部落冲突资源并按阈值选择进攻目标
- 游戏更新后重新校准按钮即可恢复使用
- 通过手机通知接收挂机错误与完成消息

## 场景标签

`GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L3: A **thread-safe** automation bot for Clash of Clans farming on LDPlayer. It screenshots the emulator through **ADB**
> L10: - **YOLO + OCR for dynamic content**: base layout, Gold/Elixir/Dark Elixir values, post-battle loot are still detec

## 星数曲线

```mermaid
xychart-beta
    title "anugrhaswi/Coc-Auto-Farm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-28 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `9f8c5d1657c3` · [字段定义](../../DATASET.md)*
