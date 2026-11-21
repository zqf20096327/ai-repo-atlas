# abozaralizadeh/Felinquent

⭐ 9 · TypeScript · NOASSERTION · 推送 2026-11-20 · [GitHub](https://github.com/abozaralizadeh/Felinquent) · [官网](https://abozaralizadeh.github.io/Felinquent/) · 个人维护

**macOS/Windows 桌面宠物：在真实窗口上自主活动的动物**

基于 Tauri 的透明覆盖层桌面宠物应用，支持 9 个内置角色（猫/狗/狐狸/浣熊/兔/松鼠），可 interacting：抚摸、戳、抛玩具、喂零食等；行为由规则大脑驱动，可选接入本地 Ollama 模型生成计划与想法气泡，移除模型后行为仍完整运行。声明不模拟键鼠输入、不截屏，支持会议/屏幕共享时自动隐藏与 Panic 热键。提供 Mac/Windows 安装包、终端脚本安装与浏览器 playground。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 9 个内置角色，各有专属本能与动作序列
- 可选本地 Ollama 模型规划行为，规则大脑为默认回退
- 不模拟输入、不截屏，CI 检查禁止伪造输入代码
- 支持 .felinquent 角色包扩展，仅作数据加载并逐文件校验

## 适用场景

- 在 macOS/Windows 桌面上养一只自主活动的宠物
- 会议或屏幕共享时让它自动隐藏不打扰
- 本地运行 LLM 给宠物生成行为计划和想法气泡
- 用浏览器 playground 无安装体验完整行为系统

## 场景标签

 · 领域:桌面工具/娱乐

## 证据(README 行号)

> L29: **Status: early.** The brain, rules, movement and animation are built and tested, and a browser playground runs all
> L64: - Everything runs locally. No accounts, no cloud. On its own it fetches the update check, a small file from GitHub 

## 星数曲线

```mermaid
xychart-beta
    title "abozaralizadeh/Felinquent 星数(近 3 点)"
    x-axis ["2026-11-08", "2026-11-10", "2026-11-21"]
    y-axis "stars" 7 --> 10
    line [8, 9, 9]
```

2026-11-08 8 → 2026-11-21 9（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `812645be0a4b` · [字段定义](../../DATASET.md)*
