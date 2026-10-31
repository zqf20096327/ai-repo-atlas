# VORNEX-01/JARVIS-VORNEX

⭐ 22 · Python · NOASSERTION · 推送 2026-10-03 · [GitHub](https://github.com/VORNEX-01/JARVIS-VORNEX) · [官网](https://instagram.com/vornex_web) · 组织维护

**Windows 语音桌面 AI 助手：对话操控电脑并自动验证结果**

由 VORNEX 开发的 Windows 语音桌面助手：用户以语音下达指令，系统按 观察→理解→行动→验证 循环执行打开应用、操作窗口键鼠、管理文件、网页搜索、消息与媒体工作流、系统监控恢复及编码辅助等多步任务。通用桌面控制层基于标准桌面控件工作，无需为每个应用单独写脚本；无法确认结果时会停止而非声称成功。依赖 Gemini API（最多配三把 key）、Python 3.11+ 与麦克风，含带鉴权的远程仪表板，API key 本地存储不入 Git。从源码克隆并 pip 安装依赖后运行 main.py。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 观察→理解→行动→验证 循环，行动后核验结果
- 通用桌面控制层直接操作标准 Windows 控件，无需逐应用脚本
- 支持配置最多三个 Gemini API key，凭据仅本地存储
- 带鉴权的远程仪表板，不暴露 Gemini 凭据

## 适用场景

- 用语音让助手代为操作电脑完成多步任务
- 远程通过仪表板查看和管理工作流
- 让 AI 协助编码与开发相关操作

## 场景标签

`语音 Agent` `AI 助手` `GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L18: It is built to work with your computer directly — opening applications, navigating interfaces, handling files, usin
> L22: > **Tell JARVIS what you need. Let it handle the computer.**
> L47: **Observe → Understand → Act → Verify**

## 星数曲线

```mermaid
xychart-beta
    title "VORNEX-01/JARVIS-VORNEX 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-31 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `87607722567f` · [字段定义](../../DATASET.md)*
