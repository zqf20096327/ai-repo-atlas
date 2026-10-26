# 777genius/os-ai-computer-use

⭐ 184 · Python · Apache-2.0 · 推送 2026-05-26 · [GitHub](https://github.com/777genius/os-ai-computer-use) · 个人维护

**让 AI 直接操控桌面（点击/输入/截屏）的跨平台代理应用**

跨平台桌面自动化代理：通过 OpenAI 或 Anthropic 的 Computer Use 能力控制用户操作系统，执行点击、输入、滚动、拖拽与截屏等操作。提供面向终端用户的 Flutter 桌面应用（macOS/Windows/Linux/Web 安装包）与 Python CLI 两种使用方式，架构上 provider 无关，新增模型只需实现 LLMClient 接口。README 报告 OSWorld 基准 75.0%。限制：需 X11/XWayland（纯 Wayland 未支持）、Windows 驱动尚未完成集成测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- OpenAI 与 Anthropic 双 provider，可在设置中切换
- 跨平台 Flutter UI + Python CLI + WebSocket/JSON-RPC 后端
- provider 无关架构：新增 llm_<provider> 包即可接入新模型
- macOS/Windows/Linux/Web 提供发布版安装包

## 适用场景

- 用自然语言任务让 AI 代为操作桌面应用
- 在浏览器中搜索、打开结果并截图等自动化流程
- 对比不同模型在桌面任务上的成本与表现

## 场景标签

`GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L29: - 🖥️ AI controls your desktop: clicks, types, scrolls, drags, takes screenshots
> L106: python -m os_ai_cli --provider openai --task "Open Safari and search for 'AI news'"

## 星数曲线

```mermaid
xychart-beta
    title "777genius/os-ai-computer-use 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 183 --> 185
    line [184, 184]
```

2026-10-18 184 → 2026-10-26 184（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `269148c59664` · [字段定义](../../DATASET.md)*
