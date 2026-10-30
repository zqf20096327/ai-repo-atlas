# ToryPan/ask-open-webui-everywhere

⭐ 48 · JavaScript · MIT · 推送 2026-01-05 · [GitHub](https://github.com/ToryPan/ask-open-webui-everywhere) · 个人维护

**将 Open WebUI 嵌入浏览器侧栏、随时对网页提问的扩展**

浏览器扩展：把用户自部署的 Open WebUI 实例加载到浏览器侧边栏，实现不切换标签页的网页问答。提供两个上下文注入功能：Insert Text 解析当前网页正文（过滤 SCRIPT/NAV 等标签）并以 .txt 文件附件形式送入聊天，借助模拟粘贴触发 Open WebUI 的超长文本转文件机制；Insert Screen 用 chrome.tabs.captureVisibleTab 截取可见区域并以粘贴事件注入图片。需手动配置实例 URL 并以开发者模式加载未打包源码，已在 Edge/Chrome 143+ 验证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 侧边栏内嵌自部署 Open WebUI 实例
- 一键解析网页正文并作为文件附件发送
- 一键截取当前标签页可见区域作为图片上下文
- 正文提取过滤 12 类噪声 HTML 标签

## 适用场景

- 浏览网页时在侧栏直接向自己的 Open WebUI 提问
- 把当前页面正文或截图作为上下文发给 AI 分析
- 减少网页与聊天界面之间的复制粘贴切换

## 场景标签

`文档问答` `聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L3: **AOE** is a browser extension designed to integrate Open WebUI directly into your browsing experience.
> L7: **AOE** solves this by opening your Open WebUI instance in the browser's side panel, allowing you to interact with A
> L63: ## How it Works

## 星数曲线

```mermaid
xychart-beta
    title "ToryPan/ask-open-webui-everywhere 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 47 --> 49
    line [48, 48]
```

2026-10-18 48 → 2026-10-30 48（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `540d5e8c0b95` · [字段定义](../../DATASET.md)*
