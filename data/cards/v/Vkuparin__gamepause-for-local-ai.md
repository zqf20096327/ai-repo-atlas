# Vkuparin/gamepause-for-local-ai

⭐ 25 · Rust · MIT · 推送 2026-10-18 · [GitHub](https://github.com/Vkuparin/gamepause-for-local-ai) · 个人维护

**游戏时自动暂停本地 AI 服务、结束后恢复的 Windows 托盘应用**

原生 Windows 托盘应用：检测 Steam、Epic、GOG 等平台及自定义程序启动的游戏后，保存 LM Studio、Ollama、Hermes 的模型加载状态并暂停释放 VRAM，游戏退出 30 秒后自动恢复；也可指定 llama-server.exe、koboldcpp.exe 等程序按原命令行重启。LM Studio 恢复模型标识/TTL/加载配置，Ollama 恢复 GGUF 模型及剩余 keep-alive 时间（嵌入模型不恢复）。崩溃恢复状态先落盘。仅本地运行，无遥测。面向同时使用本地大模型与游戏的 Windows 用户。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 游戏启动自动暂停、退出后恢复 LM Studio/Ollama/Hermes 的模型加载状态
- 崩溃可恢复：卸载前状态写盘，重启后继续完成恢复
- Steam/Epic/GOG/Xbox 等 7 平台游戏自动检测，支持按游戏设规则与全局快捷键
- 仅本地运行，无遥测、无管理员服务

## 适用场景

- 玩大型游戏时释放被本地 AI 占用的显存
- 常驻本地 AI 助手与游戏共用一台机器，希望游戏结束自动恢复模型
- 为 llama-server/koboldcpp 等自选 AI 服务配置游戏时自动停止与重启

## 场景标签

 · 领域:桌面工具/本地 AI 运维

## 证据(README 行号)

> L9: GamePause is a small native Windows tray app. When a game starts, it saves the supported state of your local AI prov
> L19: - **LM Studio, restored exactly.** Every loaded LLM and embedding model returns with the same identifier, variant, 
> L20: - **Ollama, when it is running.** Local models are unloaded. GGUF completion models are reloaded with their context

## 星数曲线

```mermaid
xychart-beta
    title "Vkuparin/gamepause-for-local-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-28 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `757f9c366111` · [字段定义](../../DATASET.md)*
