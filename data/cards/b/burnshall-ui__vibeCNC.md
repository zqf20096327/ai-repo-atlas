# burnshall-ui/vibeCNC

⭐ 13 · Python · Apache-2.0 · 推送 2026-08-25 · [GitHub](https://github.com/burnshall-ui/vibeCNC) · 个人维护

**给机加工人员的 Fanuc 风格 CNC 车床模拟器，附 AI G 代码辅助**

基于 Python/PyQt6 的 Fanuc 风格 CNC 车床模拟桌面应用：逐行渐进刀具路径绘制、实时 X/Z/主轴/进给显示、卡盘碰撞警告、G41/G42 刀尖半径补偿、语法高亮与自动补全、刀具/宏库与策略引擎，可选集成 CAMotics 3D 模拟。AI 部分支持 Claude（云）与 Ollama（本地）双通道，提供 G 代码安全审查与自然语言生成代码片段。README 明确声明碰撞检测与 AI 审查为启发式，不证明程序安全，禁止未验证即在真机运行。安装需 git clone 源码并自行运行，要求 Python 3.10+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 逐行渐进刀具路径绘制与实时位置显示
- Claude（云）与 Ollama（本地）双 AI 通道：G 代码审查与自然语言生成
- G41/G42 刀尖半径补偿（含圆弧与拐角处理）
- Fanuc 风格控制面板（CYCLE START/FEED HOLD/SINGLE BLOCK）与策略引擎

## 适用场景

- 在电脑上模拟和调试 Fanuc 风格车床 G 代码程序
- 让 AI 审查程序的安全隐患或从自然语言生成代码片段
- 管理刀具表与常用宏，配合 CAMotics 做 3D 模拟

## 场景标签

`代码生成` `代码审查` · 领域:编码与开发

## 证据(README 行号)

> L12: **A modern, Fanuc-style CNC simulator with AI-powered G-Code assistance**
> L41: - **Dual AI Support** - Works with both Claude (cloud) and Ollama (local)

## 星数曲线

```mermaid
xychart-beta
    title "burnshall-ui/vibeCNC 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `1788458e1dbf` · [字段定义](../../DATASET.md)*
