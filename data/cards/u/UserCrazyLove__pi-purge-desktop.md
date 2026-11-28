# UserCrazyLove/pi-purge-desktop

⭐ 3 · JavaScript · MIT · 推送 2026-11-04 · [GitHub](https://github.com/UserCrazyLove/pi-purge-desktop) · [官网](https://github.com/UserCrazyLove/pi-purge-desktop#readme) · 个人维护 · 中文 README

**PI-Desktop 插件：为 pi 会话换装系统提示词**

面向 PI-Desktop v0.21.0 的插件，把 pi 会话的系统提示词纳入可视控制：strict/replace/append 三种组合模式决定 persona 文本与 harness 提示词的保留比例，支持从内置示例、本地文件或目录读取 persona，配置持久化到宿主插件数据目录，并在每轮对话后显示身份段/文档段是否被裁剪、发送前后字符数等工作目录遥测。离线运行，无网络权限；依赖宿主的 agent.extension 高风险权限重写出站提示词。附 /purge CLI 扩展与面板双入口。

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

- strict/replace/append 三种系统提示词组合模式
- 文件/目录/拖拽方式加载 persona，面板预览与校验
- 每轮对话的实况遥测：裁剪段落与字符数
- 完全离线：无网络权限、无遥测、无自动更新

## 适用场景

- 给 pi 会话换用自定义 persona 而不破坏工具上下文
- 隔离系统提示词变量做行为对照实验
- 通过面板随时查看本轮提示词被改写成了什么

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L11: A PI-Desktop plugin that puts the system prompt of a pi session behind a switch, and behind a panel you can actuall
> L35: |**Three composition modes**|`strict` (persona + working directory only), `replace` (persona + harness prompt minus
> L125: |`agent.extension`|high|Loads the extension inside the Agent sidecar. With Node access, it rewrites the system pro

## 星数曲线

```mermaid
xychart-beta
    title "UserCrazyLove/pi-purge-desktop 星数(近 2 点)"
    x-axis ["2026-11-27", "2026-11-28"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-27 3 → 2026-11-28 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `6701e4086269` · [字段定义](../../DATASET.md)*
