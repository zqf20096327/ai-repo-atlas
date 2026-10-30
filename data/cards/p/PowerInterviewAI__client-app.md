# PowerInterviewAI/client-app

⭐ 15 · TypeScript · MIT · 推送 2026-10-15 · [GitHub](https://github.com/PowerInterviewAI/client-app) · [官网](https://www.powerinterviewai.com) · 组织维护

**面向求职者的实时 AI 面试助手：实时转录与提示建议**

Electron 桌面客户端，配合自有后端（FastAPI/MongoDB/Redis，含 ASR 与 LLM 服务）提供双通道实时语音转录、基于简历与职位描述的流式回答建议、截图理解与代码解答（支持最多 4 张截图）。强调隐私：转写不落盘、仅内存保存，账号配置跨设备同步，本地设置写入用户数据目录。提供隐身模式隐藏窗口防屏幕共享捕获。Windows 提供 x64 安装包，macOS 14.4+ 提供签名发布件，也支持源码运行（Node.js 22.15+/pnpm）。

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

- 双通道实时转录（说话人检测、WebSocket 流式）
- 基于 CV 与职位描述的实时个性化建议（提示式或整句式）
- 截图理解 + LLM 生成代码方案（最多 4 图，语法高亮输出）
- 隐身模式：隐藏窗口、任务栏按钮与 Dock 图标

## 适用场景

- 技术面试中获取代码提示与调试协助
- 行为面试中获得基于个人简历的实时回答建议
- 面试练习时通过转录自我监控与复盘

## 场景标签

`语音识别` `AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L14: Power Interview is a privacy-first AI assistant designed to help you ace technical and behavioral interviews. With 
> L31: Stay on top of the conversation with live ASR:
> L94: - AI/LLM Service for suggestions

## 星数曲线

```mermaid
xychart-beta
    title "PowerInterviewAI/client-app 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `43c2e53d46fd` · [字段定义](../../DATASET.md)*
