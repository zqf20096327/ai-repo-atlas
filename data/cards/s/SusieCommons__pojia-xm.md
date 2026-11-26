# SusieCommons/pojia-xm

⭐ 3 · Python · MIT · 推送 2026-11-25 · [GitHub](https://github.com/SusieCommons/pojia-xm) · 个人维护 · 中文 README

**Windows 工具：替换四个 AI 客户端的内置系统提示词**

面向 Windows 的 GUI/CLI 工具，将 Codex、WorkBuddy、ZCode、DSH 四个客户端启动时读入的内置提示词，替换为用户自写的 persona.md，四个客户端共用一份人格源。注入方式均为各客户端提供的文本配置入口（config.toml 键、模板段替换、用户级 AGENTS.md），不修改二进制。提供写入前备份、按标记还原、自检口令验证、原子写与 UTF-8 编码处理；全程不联网。提供预编译 exe 与源码运行两种方式，仅支持 Windows，不支持 macOS/Linux。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四个客户端共用一份 persona.md，口径一致
- 先备份再写入，支持按标记还原且不依赖备份
- 固定口令自检机制验证注入真实生效
- 全程零网络请求，支持 --dry 演练不写盘

## 适用场景

- 让多个 AI 客户端使用同一份自定义身份设定
- 客户端升级覆盖配置后重新注入提示词
- 需验证提示词真实载入而非表面生效的场景

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: **把你电脑上那几个 AI 客户端「自己改不到的内置提示词」，换成你自己写的那份 —— 点一个按钮的事。**
> L6: 支持 **Codex / WorkBuddy / ZCode / DSH** 四个客户端，一份 `persona.md` 全管，口径一致。
> L166: |`codex`|Codex（OpenAI CLI / 桌面端）|官方 `config.toml` 的 `model_instructions_file` 指向人格文件|


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `7b96aaa4808a` · [字段定义](../../DATASET.md)*
