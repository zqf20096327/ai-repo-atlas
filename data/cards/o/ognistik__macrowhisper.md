# ognistik/macrowhisper

⭐ 227 · Swift · GPL-3.0 · 推送 2026-10-15 · [GitHub](https://github.com/ognistik/macrowhisper) · 个人维护

**Superwhisper 听写结果的自动化助手：按规则执行粘贴/开链接/跑脚本**

macOS 上的命令行后台服务，监视 Superwhisper 保存的录音文件夹，读取转写结果后按规则执行动作：粘贴或键入文本、打开 URL、运行 macOS 快捷指令、shell 命令或 AppleScript，并可链式组合。动作按语音短语、前台应用、Superwhisper 模式、浏览器 URL 或默认回退动作选择。JSON 配置（configVersion 3，旧版自动迁移），需 macOS 12.4+、Superwhisper 及辅助功能权限；通过 Homebrew 或安装脚本安装预编译可执行文件。项目独立于 Superwhisper，无隶属关系。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 监视 Superwhisper 录音文件夹并读取最终转写结果 {{swResult}}
- 动作链：粘贴/键入、打开 URL、Shortcuts、shell、AppleScript
- 按语音短语、前台应用、模式、URL 多级触发与优先级排序
- 提供 Homebrew、安装脚本（SHA-256 校验）与 CLI 服务管理命令

## 适用场景

- 把语音听写自动粘贴到当前输入框
- 用语音短语触发快捷指令或打开网页搜索
- 按前台应用或浏览器 URL 自动切换听写后的动作

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L3: Macrowhisper is an automation helper for Superwhisper. Superwhisper turns your voice into text; Macrowhisper watches
> L5: It can paste or type the result, open a URL, run a macOS Shortcut, run a shell command or AppleScript, and chain sev

## 星数曲线

```mermaid
xychart-beta
    title "ognistik/macrowhisper 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 226 --> 228
    line [227, 227]
```

2026-10-18 227 → 2026-10-28 227（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `fe82b9236474` · [字段定义](../../DATASET.md)*
