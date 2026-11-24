# xdtbp/DaFeiYu

⭐ 7 · TypeScript · NOASSERTION · 推送 2026-11-23 · [GitHub](https://github.com/xdtbp/DaFeiYu) · 个人维护 · 中文 README

**为手机用户提供的仿 DeepSeek App 第三方安卓对话客户端**

基于 DeepSeek 官方开源网页示例（chat-demo）二次开发的 Android 客户端，采用 Kotlin WebView 壳 + 内置前端资源的架构，为移动端适配官方 App 的交互逻辑。对话功能支持流式输出、深度思考折叠、联网搜索、Markdown/KaTeX/Mermaid 渲染与模型切换；提供拍照圈画标注、多选传图、语音输入（AudioRecord 录音 + 官方 ASR）；支持 Harness 账号 OAuth PKCE 登录或手动填写 API Key，并可导入/导出官方历史 ZIP。构建需 Node.js 22+、pnpm、JDK 17 与 Android SDK。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- WebView 壳 + 原生能力桥（相册、主题、登录、文件、唤醒锁、语音）架构
- 圈画标注全屏编辑器与拍照/相册多选上传
- Harness 账号 OAuth PKCE 登录，无需手动填 API Key
- 官方历史 ZIP 导入/导出，512KB 分块流式写入下载目录

## 适用场景

- 在 Android 手机上以接近官方 App 的方式使用 DeepSeek 对话
- 拍照圈画向 AI 提问并管理图片附件
- 备份与迁移官方导出的对话历史

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L17: > 基于 DeepSeek 官方前端示例（`chat-demo`）改造的安卓客户端，应用显示名为「大肥鱼」，与官方品牌无关联。原生 WebView 壳 + 前端资源内置，配合一组原生能力桥，得到接近官方 App 的移动端体验。
> L38: * 流式输出、停止生成、重新生成、分支切换（来自官方前端）
> L43: * 模型切换：`API Key` 或 `Harness 账号` × `DeepSeek-V4.1-Flash` / `DeepSeek-V4-Pro`


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `2cf2300bd4c8` · [字段定义](../../DATASET.md)*
