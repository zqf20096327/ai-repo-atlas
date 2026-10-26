# precious112/caret-desktop

⭐ 38 · TypeScript · Apache-2.0 · 推送 2026-10-18 · [GitHub](https://github.com/precious112/caret-desktop) · [官网](https://caretai.cloud) · 个人维护

**本地运行的桌面设计画布：在代码渲染的页面上直接改设计并写回源文件**

Electron 桌面应用，把仓库中的页面渲染为可交互画布：右键改文本/颜色/尺寸后写入 .caret/ 下的真实 React 代码，颜色可匹配设计 token；可框选区域用自然语言让 AI agent 修改、并发生成三个版本、生成图片/矢量/动画背景资产；通过双向同步把设计合入任意框架的应用，并以 MCP 暴露给 Claude Code、Codex 等外部 agent。模型自带接入（OpenCode 引擎），可用 API key 或订阅登录。需 Node.js 20.19+ 才能运行实时画布；Windows 构建未代码签名。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 页面直改（文本/颜色/图像/尺寸）直接写入源文件，颜色可匹配设计 token
- 框选区域用自然语言描述，交给 AI agent 完成复杂修改，可同时生成三个版本对比
- 通过 MCP 将设计层暴露给外部 agent（Claude Code、Codex 已测试）
- 内置 OpenCode 引擎，支持 API key 或订阅（ChatGPT Plus/Pro/Go、Kimi、Z.AI、Zhipu、GitHub Copilot）登录

## 适用场景

- 在真实代码渲染的页面上直接微调设计并保留在 git 中可审阅
- 用自然语言让 agent 生成多个设计版本再挑选保留
- 生成与设计 token 一致的 logo、照片、纹理与动画背景
- 把外部终端 agent（Claude Code/Codex）通过 MCP 接入做设计同步

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L18: Your pages render on a canvas. Click a headline and retype it, right-click a
> L19: colour and pick a new one, and the change is written into the file behind it.
> L22: That design lives in your repo as real React, in `.caret/`, in git, reviewable
> L35: Free, runs on your machine, no account. Needs Node.js

## 星数曲线

```mermaid
xychart-beta
    title "precious112/caret-desktop 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-26"]
    y-axis "stars" 36 --> 39
    line [37, 38, 38]
```

2026-10-18 37 → 2026-10-26 38（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `f6fb1e49a1f4` · [字段定义](../../DATASET.md)*
