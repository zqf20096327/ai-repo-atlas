# lemoony/snipkit

⭐ 120 · Go · Apache-2.0 · 推送 2026-05-01 · [GitHub](https://github.com/lemoony/snipkit) · 个人维护

**终端内片段管理器：搜索、执行与 AI 生成 shell 脚本片段**

用 Go 编写的命令行片段管理工具：从 SnippetsLab、Snip、GitHub Gist、Pet、MassCode 或文件系统目录加载片段，支持标签过滤、按输入搜索、参数替换（枚举/密码掩码/路径自动补全）与主题定制；核心命令为 exec/print，可在终端内直接执行片段。AI 部分为 BETA 阶段的 SnipKit Assistant：通过聊天式界面按提示生成带参数的脚本，支持 OpenAI、Anthropic、Google Gemini、Ollama 及任意 OpenAI 兼容 API，并提供独立的 SnipKit GPT。安装途径包括 Homebrew、apt、yum、deb/rpm/apk 包、go install 与源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 接入 6 种外部片段来源（SnippetsLab/Gist/Pet/MassCode 等）
- BETA 的 SnipKit Assistant 按提示生成带参数脚本，支持 5 类 AI 提供商
- 参数替换支持枚举、密码掩码与路径自动补全
- 多平台安装途径：Homebrew/apt/yum/deb/rpm/apk/go install/源码构建

## 适用场景

- 把常用 shell 命令存为带参数片段，终端内搜索即执行
- 用 AI 按自然语言提示生成脚本并保存到片段库
- 整合已有的 Gist/Pet/MassCode 片段到统一入口

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L5:  Execute the scripts saved in your favorite snippet manager or generate new scripts with the help of AI without even
> L40: ### SnipKit Assistant (BETA) 🤖

## 星数曲线

```mermaid
xychart-beta
    title "lemoony/snipkit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 119 --> 121
    line [120, 120]
```

2026-10-18 120 → 2026-10-23 120（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `e6c92bc5fdd4` · [字段定义](../../DATASET.md)*
