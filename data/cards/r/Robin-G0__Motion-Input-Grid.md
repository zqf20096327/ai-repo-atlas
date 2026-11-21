# Robin-G0/Motion-Input-Grid

⭐ 9 · JavaScript · Apache-2.0 · 推送 2026-11-20 · [GitHub](https://github.com/Robin-G0/Motion-Input-Grid) · 个人维护

**摄像头姿态追踪的体势动作输入框架，动作映射为操作**

开源动作输入框架：基于摄像头身体姿态追踪，将手部或身体部位的运动轨迹识别为可配置动作，输出到网站、桌面应用与游戏，并可发送系统键盘快捷键。核心机制：在网页或桌面 Studio 中为部位绘制路径条件（必经/禁行/触发/手势交互），导出 JSON 配置后由 Windows/Linux x64 桌面 Controller 追踪执行；识别引擎为 C++20 实现，经 PyPI/npm 提供 Python/WASM 集成。状态为早期开发，Linux 桌面应用与游戏引擎集成待更广泛测试；Linux 键盘输出依赖 X11，Wayland 原生输出不可用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 路径式手势条件定义（必经/禁行/触发/手势交互）并导出 JSON 配置
- 摄像头画面在本机处理，需下载追踪模型
- Python (PyPI) 与 JavaScript (npm/WASM) 集成，同一 C++20 识别引擎
- 支持 Unity/Unreal/Godot 等引擎集成（标记为 Preview）

## 适用场景

- 用手势控制演示文稿翻页（Canva/PowerPoint/PDF）
- 以现有键盘映射控制游戏
- 日常电脑操作中用手势触发快捷键

## 场景标签

`GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L5: Motion Input Grid is an open-source motion input framework. It turns tracked body
> L18: then recognize it with a camera. Use the resulting actions in your project or send
> L78: Every integration uses the same C++20 recognition engine and JSON profiles.

## 星数曲线

```mermaid
xychart-beta
    title "Robin-G0/Motion-Input-Grid 星数(近 3 点)"
    x-axis ["2026-10-19", "2026-10-22", "2026-11-21"]
    y-axis "stars" 7 --> 10
    line [8, 9, 9]
```

2026-10-19 8 → 2026-11-21 9（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `40dbfcac6369` · [字段定义](../../DATASET.md)*
