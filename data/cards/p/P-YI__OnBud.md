# P-YI/OnBud

⭐ 13 · TypeScript · MIT · 推送 2026-11-17 · [GitHub](https://github.com/P-YI/OnBud) · 个人维护 · 中文 README

**macOS 本地端侧 AI 启动器：用苹果内置模型检索与操作本机文件**

基于 Apple FoundationModels（经 apfel 调用 Apple silicon 内置约 3B 模型）的 Spotlight 风格面板（⌥ Space），面向 Apple silicon + macOS 26 用户提供本地文件问答与操作代理。机制：13 个带权限契约的技能包（文件/代码/git/系统操作等），所有命令、编辑、网络查询与不可逆操作需逐条批准；默认不离开本机，可选插件接入路由小模型、GitHub Copilot、Codex（经 OpenCode）、SearXNG 搜索、MacTeX 与远程 GPU 服务器。提供 Homebrew cask 与 DMG 安装，未做签名公证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 调用 Apple 内置端侧模型（apfel），默认计算不离开本机
- 13 个技能包带权限契约，命令/编辑/网络查询均需逐项批准
- 插件体系：路由小模型、GitHub Copilot、Codex via OpenCode、SearXNG、MacTeX、远程服务器
- 同一控制器可作为 OpenCode agent（afm）与 MCP 服务器

## 适用场景

- 按 ⌥ Space 询问文件夹、论文、表格或未提交的 git 变更
- 用自然语言执行 Mac 操作（音量、Wi-Fi、打开应用等）并逐条确认
- 经 SSH 把实验命令上传到自己的 GPU 服务器，审批后运行并跟踪日志
- 在任意应用中选中文本通过 Services 菜单向本地模型提问

## 场景标签

`AI 助手` `编码 Agent` `文档问答` · 领域:编码与开发

## 证据(README 行号)

> L3:  Apple's on-device model, put to work on your own files.
> L18: Every Apple silicon Mac with Apple Intelligence has a ~3B language model built in. On its own it is a good
> L19: reader and a weak programmer. **OnBud** wraps it in code that does the searching, reading, running and

## 星数曲线

```mermaid
xychart-beta
    title "P-YI/OnBud 星数(近 2 点)"
    x-axis ["2026-11-10", "2026-11-24"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-10 3 → 2026-11-24 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `e4b4738c505e` · [字段定义](../../DATASET.md)*
