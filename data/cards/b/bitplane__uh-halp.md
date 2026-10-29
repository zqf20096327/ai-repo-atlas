# bitplane/uh-halp

⭐ 20 · Python · NOASSERTION · 推送 2026-07-30 · [GitHub](https://github.com/bitplane/uh-halp) · [官网](https://bitplane.net/dev/python/uh-halp) · 个人维护

**用 LLM 生成 shell 命令的命令行工具**

命令行工具：用户以自然语言描述想做的事，工具调用所选 LLM 生成对应 shell 命令并输出。默认后端为 Groq，首次使用时保存 API key 到 ~/.uh-keys；可通过编辑 ~/.uh-config 切换后端，或以带 query 函数的模块自定义后端。以 Python 包形式经 pip 安装。README 声明在 Linux 与 macOS 的 bash/zsh 下测试，其他平台未充分测试，并提示不要未经阅读直接执行生成结果。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言转 shell 命令的命令行工具
- 默认 Groq 后端，支持自定义后端模块（query 函数 + 模板参数）
- key 保存于 ~/.uh-keys，配置于 ~/.uh-config

## 适用场景

- 忘记命令语法时用一句话查出对应命令
- 不常用系统上快速生成 shell 操作命令
- 通过自定义后端接入自选 LLM 服务

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L20: $ uh reverse file.txt
> L37: It currently defaults to Groq. If you want to use something else, open

## 星数曲线

```mermaid
xychart-beta
    title "bitplane/uh-halp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-29 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `87a77aa01e56` · [字段定义](../../DATASET.md)*
